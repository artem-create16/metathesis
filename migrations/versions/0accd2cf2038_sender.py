"""Sender

Revision ID: 0accd2cf2038
Revises: 77a0fd667bc9
Create Date: 2021-07-17 23:15:29.287843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0accd2cf2038'
down_revision = '77a0fd667bc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('sender', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'messages', 'users', ['sender'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.drop_column('messages', 'sender')
    # ### end Alembic commands ###
