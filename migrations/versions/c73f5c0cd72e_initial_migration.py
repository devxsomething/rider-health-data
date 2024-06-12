"""initial migration

Revision ID: c73f5c0cd72e
Revises: 
Create Date: 2024-06-12 15:41:53.796812

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c73f5c0cd72e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pwd', sa.String(length=300), nullable=False))
    op.drop_index('password', table_name='users')
    op.create_unique_constraint(None, 'users', ['pwd'])
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(length=300), nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.create_index('password', 'users', ['password'], unique=False)
    op.drop_column('users', 'pwd')
    # ### end Alembic commands ###
