"""Add table users

Revision ID: bdbb017ff39a
Revises: 3548a0aa37d0
Create Date: 2023-12-23 14:26:23.449778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdbb017ff39a'
down_revision: Union[str, None] = '3548a0aa37d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('contacts', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('contacts', sa.Column('update_at', sa.DateTime(), nullable=True))
    op.add_column('contacts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contacts', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_column('contacts', 'user_id')
    op.drop_column('contacts', 'update_at')
    op.drop_column('contacts', 'created_at')
    op.drop_table('users')
    # ### end Alembic commands ###