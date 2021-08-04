"""Fixed message table

Revision ID: 0e53eac0828b
Revises: abb8557c4738
Create Date: 2021-07-28 16:28:06.697498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e53eac0828b'
down_revision = 'abb8557c4738'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('recipient_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'messages', 'users', ['recipient_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.drop_column('messages', 'recipient_id')
    # ### end Alembic commands ###
