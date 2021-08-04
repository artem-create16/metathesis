"""Messages fixed

Revision ID: 3c85f18e5fa8
Revises: 0e53eac0828b
Create Date: 2021-07-29 21:05:18.967405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c85f18e5fa8'
down_revision = '0e53eac0828b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('messages', sa.Column('interlocutor_id', sa.Integer(), nullable=True))
    op.drop_constraint('messages_sender_id_fkey', 'messages', type_='foreignkey')
    op.drop_constraint('messages_recipient_id_fkey', 'messages', type_='foreignkey')
    op.create_foreign_key(None, 'messages', 'users', ['interlocutor_id'], ['id'])
    op.create_foreign_key(None, 'messages', 'users', ['user_id'], ['id'])
    op.drop_column('messages', 'sender_id')
    op.drop_column('messages', 'recipient_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('recipient_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('messages', sa.Column('sender_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.create_foreign_key('messages_recipient_id_fkey', 'messages', 'users', ['recipient_id'], ['id'])
    op.create_foreign_key('messages_sender_id_fkey', 'messages', 'users', ['sender_id'], ['id'])
    op.drop_column('messages', 'interlocutor_id')
    op.drop_column('messages', 'user_id')
    # ### end Alembic commands ###