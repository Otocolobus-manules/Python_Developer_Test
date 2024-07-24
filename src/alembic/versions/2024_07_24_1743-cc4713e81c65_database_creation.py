"""Database creation

Revision ID: cc4713e81c65
Revises: 
Create Date: 2024-07-24 17:43:43.283836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc4713e81c65'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )


def downgrade() -> None:
    op.drop_table('user')
