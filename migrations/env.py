import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel


from app.heroes.models import Hero


cfg = context.config
if cfg.config_file_name is not None:
    fileConfig(cfg.config_file_name)


target_metadata = SQLModel.metadata
target_metadata.naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


url = cfg.get_main_option("sqlalchemy.url")

print("Database URL:", url)

def run_migrations_offline() -> None:
    """Executa migrações no modo offline."""
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"}
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Executa migrações no modo online."""
    
    config_section = cfg.get_section(cfg.config_ini_section)
    config_section["sqlalchemy.url"] = url
    
    
    connectable = engine_from_config(
        config_section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

print("Tabelas registradas no metadata:", target_metadata.tables.keys())
