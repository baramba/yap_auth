"""empty message

Revision ID: 861577600544
Revises: 05c25ab126cc
Create Date: 2022-06-17 10:57:39.789882

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '861577600544'
down_revision = '05c25ab126cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_history')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_history',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_agent', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('auth_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_history_pkey')
    )
    # ### end Alembic commands ###
