"""fix naming

Revision ID: 947defd854c7
Revises: 91f7b28e2ab1
Create Date: 2021-07-10 10:45:02.997600

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '947defd854c7'
down_revision = '91f7b28e2ab1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ads',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ad_photos',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('ad_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ad_id'], ['ads.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link')
    )
    # op.drop_table('products')
    # op.drop_table('product_photos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_photos',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('link', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='product_photos_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='product_photos_pkey'),
    sa.UniqueConstraint('link', name='product_photos_link_key')
    )
    op.create_table('products',
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='products_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='products_pkey')
    )
    op.drop_table('ad_photos')
    op.drop_table('ads')
    # ### end Alembic commands ###
