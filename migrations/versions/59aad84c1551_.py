"""empty message

Revision ID: 59aad84c1551
Revises: 3c85f18e5fa8
Create Date: 2021-09-07 13:35:58.558914

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '59aad84c1551'
down_revision = '3c85f18e5fa8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('subject', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('ad_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('interlocutor_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ad_id'], ['ads.id'], name='messages_ad_id_fkey'),
    sa.ForeignKeyConstraint(['interlocutor_id'], ['users.id'], name='messages_interlocutor_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='messages_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='messages_pkey')
    )
    # ### end Alembic commands ###