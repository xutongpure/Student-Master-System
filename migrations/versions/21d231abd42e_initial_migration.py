"""initial migration

Revision ID: 21d231abd42e
Revises: 
Create Date: 2020-05-13 21:57:29.189784

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '21d231abd42e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('picture',
    sa.Column('PictureName', sa.String(length=100), nullable=False),
    sa.Column('PictureType', sa.String(length=10), nullable=False),
    sa.Column('RenderTime', sa.String(length=100), nullable=False),
    sa.Column('PicturePath', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('PictureName')
    )
    op.drop_table('wenjian')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wenjian',
    sa.Column('wenjian', mysql.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('wenjian'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('picture')
    # ### end Alembic commands ###