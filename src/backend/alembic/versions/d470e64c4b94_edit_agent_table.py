"""edit agent table

Revision ID: d470e64c4b94
Revises: 12ce57e1935a
Create Date: 2024-06-19 13:12:09.965012

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd470e64c4b94'
down_revision: Union[str, None] = '12ce57e1935a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_store_store_id', table_name='store')
    op.drop_index('ix_store_user_id', table_name='store')
    op.drop_table('store')
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_user_id', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    op.drop_index('ix_models_model_id', table_name='models')
    op.drop_index('ix_models_model_name', table_name='models')
    op.drop_index('ix_models_model_type', table_name='models')
    op.drop_index('ix_models_provider_id', table_name='models')
    op.drop_table('models')
    op.drop_index('ix_providers_company', table_name='providers')
    op.drop_index('ix_providers_description', table_name='providers')
    op.drop_index('ix_providers_name', table_name='providers')
    op.drop_index('ix_providers_provider_id', table_name='providers')
    op.drop_table('providers')
    op.drop_index('ix_credentials_credential_id', table_name='credentials')
    op.drop_index('ix_credentials_provider_id', table_name='credentials')
    op.drop_index('ix_credentials_user_id', table_name='credentials')
    op.drop_table('credentials')
    op.drop_index('ix_chain_chain_id', table_name='chain')
    op.drop_table('chain')
    op.drop_index('ix_agent_agent_id', table_name='agent')
    op.drop_index('ix_agent_user_id', table_name='agent')
    op.drop_table('agent')
    op.drop_index('ix_agents_agent_id', table_name='agents')
    op.drop_index('ix_agents_user_id', table_name='agents')
    op.drop_table('agents')
    op.drop_index('ix_inquiry_content', table_name='inquiry')
    op.drop_index('ix_inquiry_id', table_name='inquiry')
    op.drop_index('ix_inquiry_inquiry_type', table_name='inquiry')
    op.drop_index('ix_inquiry_title', table_name='inquiry')
    op.drop_table('inquiry')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inquiry',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('inquiry_type', sa.VARCHAR(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('content', sa.VARCHAR(), nullable=False),
    sa.Column('response_content', sa.VARCHAR(), nullable=True),
    sa.Column('processing_type', sa.VARCHAR(), nullable=False),
    sa.Column('creator_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updater_id', sa.INTEGER(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_inquiry_title', 'inquiry', ['title'], unique=False)
    op.create_index('ix_inquiry_inquiry_type', 'inquiry', ['inquiry_type'], unique=False)
    op.create_index('ix_inquiry_id', 'inquiry', ['id'], unique=False)
    op.create_index('ix_inquiry_content', 'inquiry', ['content'], unique=False)
    op.create_table('agents',
    sa.Column('agent_id', sa.CHAR(length=32), nullable=False),
    sa.Column('user_id', sa.CHAR(length=32), nullable=False),
    sa.Column('agent_name', sa.VARCHAR(), nullable=False),
    sa.Column('agent_description', sa.VARCHAR(), nullable=True),
    sa.Column('fm_provider_type', sa.VARCHAR(), nullable=False),
    sa.Column('fm_provider_id', sa.CHAR(length=32), nullable=False),
    sa.Column('fm_model_id', sa.CHAR(length=32), nullable=False),
    sa.Column('fm_temperature', sa.FLOAT(), nullable=False),
    sa.Column('fm_top_p', sa.FLOAT(), nullable=False),
    sa.Column('fm_request_token_limit', sa.INTEGER(), nullable=False),
    sa.Column('fm_response_token_limit', sa.INTEGER(), nullable=False),
    sa.Column('embedding_enabled', sa.BOOLEAN(), nullable=False),
    sa.Column('embedding_provider_id', sa.CHAR(length=32), nullable=True),
    sa.Column('embedding_model_id', sa.CHAR(length=32), nullable=True),
    sa.Column('storage_provider_id', sa.CHAR(length=32), nullable=False),
    sa.Column('storage_object_id', sa.CHAR(length=32), nullable=False),
    sa.Column('vector_db_provider_id', sa.CHAR(length=32), nullable=False),
    sa.Column('pre_processing_id', sa.CHAR(length=32), nullable=False),
    sa.Column('post_processing_id', sa.CHAR(length=32), nullable=False),
    sa.Column('expected_request_count', sa.INTEGER(), nullable=False),
    sa.Column('expected_token_count', sa.INTEGER(), nullable=False),
    sa.Column('expected_cost', sa.FLOAT(), nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('creator_id', sa.CHAR(length=32), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updater_id', sa.CHAR(length=32), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('agent_id')
    )
    op.create_index('ix_agents_user_id', 'agents', ['user_id'], unique=False)
    op.create_index('ix_agents_agent_id', 'agents', ['agent_id'], unique=False)
    op.create_table('agent',
    sa.Column('agent_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('agent_type', sa.VARCHAR(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.Column('is_visible_in_marketplace', sa.BOOLEAN(), nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('creator_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updater_id', sa.INTEGER(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('agent_id')
    )
    op.create_index('ix_agent_user_id', 'agent', ['user_id'], unique=False)
    op.create_index('ix_agent_agent_id', 'agent', ['agent_id'], unique=False)
    op.create_table('chain',
    sa.Column('chain_id', sa.INTEGER(), nullable=False),
    sa.Column('agent_id', sa.INTEGER(), nullable=False),
    sa.Column('provider_id', sa.INTEGER(), nullable=False),
    sa.Column('connection_order', sa.INTEGER(), nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('creator_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updater_id', sa.INTEGER(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('chain_id')
    )
    op.create_index('ix_chain_chain_id', 'chain', ['chain_id'], unique=False)
    op.create_table('credentials',
    sa.Column('credential_id', sa.CHAR(length=32), nullable=False),
    sa.Column('user_id', sa.CHAR(length=32), nullable=False),
    sa.Column('provider_id', sa.CHAR(length=32), nullable=False),
    sa.Column('credential_name', sa.VARCHAR(), nullable=False),
    sa.Column('access_key', sa.VARCHAR(), nullable=True),
    sa.Column('secret_key', sa.VARCHAR(), nullable=True),
    sa.Column('session_key', sa.VARCHAR(), nullable=True),
    sa.Column('access_token', sa.VARCHAR(), nullable=True),
    sa.Column('api_key', sa.VARCHAR(), nullable=True),
    sa.Column('api_endpoint', sa.VARCHAR(), nullable=True),
    sa.Column('is_deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('creator_id', sa.CHAR(length=32), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updater_id', sa.CHAR(length=32), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('credential_id')
    )
    op.create_index('ix_credentials_user_id', 'credentials', ['user_id'], unique=False)
    op.create_index('ix_credentials_provider_id', 'credentials', ['provider_id'], unique=False)
    op.create_index('ix_credentials_credential_id', 'credentials', ['credential_id'], unique=False)
    op.create_table('providers',
    sa.Column('provider_id', sa.CHAR(length=32), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('company', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('logo', sa.VARCHAR(), nullable=True),
    sa.Column('type', sa.VARCHAR(), nullable=False),
    sa.Column('sort_order', sa.INTEGER(), nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('creator_id', sa.CHAR(length=32), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updater_id', sa.CHAR(length=32), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('provider_id')
    )
    op.create_index('ix_providers_provider_id', 'providers', ['provider_id'], unique=False)
    op.create_index('ix_providers_name', 'providers', ['name'], unique=False)
    op.create_index('ix_providers_description', 'providers', ['description'], unique=False)
    op.create_index('ix_providers_company', 'providers', ['company'], unique=False)
    op.create_table('models',
    sa.Column('model_id', sa.CHAR(length=32), nullable=False),
    sa.Column('model_name', sa.VARCHAR(), nullable=False),
    sa.Column('provider_id', sa.CHAR(length=32), nullable=False),
    sa.Column('model_type', sa.VARCHAR(), nullable=False),
    sa.Column('sort_order', sa.INTEGER(), nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('creator_id', sa.CHAR(length=32), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updater_id', sa.CHAR(length=32), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['provider_id'], ['providers.provider_id'], ),
    sa.PrimaryKeyConstraint('model_id')
    )
    op.create_index('ix_models_provider_id', 'models', ['provider_id'], unique=False)
    op.create_index('ix_models_model_type', 'models', ['model_type'], unique=False)
    op.create_index('ix_models_model_name', 'models', ['model_name'], unique=False)
    op.create_index('ix_models_model_id', 'models', ['model_id'], unique=False)
    op.create_table('user',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('last_login', sa.DATETIME(), nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('creator_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updater_id', sa.INTEGER(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.create_index('ix_user_user_id', 'user', ['user_id'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.create_table('store',
    sa.Column('store_id', sa.CHAR(length=32), nullable=False),
    sa.Column('user_id', sa.CHAR(length=32), nullable=False),
    sa.Column('store_name', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('is_deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('creator_id', sa.CHAR(length=32), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updater_id', sa.CHAR(length=32), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('store_id')
    )
    op.create_index('ix_store_user_id', 'store', ['user_id'], unique=False)
    op.create_index('ix_store_store_id', 'store', ['store_id'], unique=False)
    # ### end Alembic commands ###
