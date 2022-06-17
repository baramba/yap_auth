"""add partitioning to users_history

Revision ID: 42370031f013
Revises: 861577600544
Create Date: 2022-06-17 12:31:28.728933

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '42370031f013'
down_revision = '861577600544'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_history',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_agent', sa.String(length=150), nullable=True),
    sa.Column('auth_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'auth_date'),
    sa.UniqueConstraint('id', 'auth_date'),
    postgresql_partition_by='RANGE (auth_date)'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_history')
    # ### end Alembic commands ###