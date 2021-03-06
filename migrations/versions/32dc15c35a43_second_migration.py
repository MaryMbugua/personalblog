"""second  migration

Revision ID: 32dc15c35a43
Revises: fe69a4d41724
Create Date: 2018-02-09 19:01:37.269057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32dc15c35a43'
down_revision = 'fe69a4d41724'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogpics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img1', sa.String(length=255), nullable=True),
    sa.Column('img2', sa.String(length=255), nullable=True),
    sa.Column('img3', sa.String(length=255), nullable=True),
    sa.Column('img4', sa.String(length=255), nullable=True),
    sa.Column('img5', sa.String(length=255), nullable=True),
    sa.Column('img6', sa.String(length=255), nullable=True),
    sa.Column('img7', sa.String(length=255), nullable=True),
    sa.Column('img8', sa.String(length=255), nullable=True),
    sa.Column('img9', sa.String(length=255), nullable=True),
    sa.Column('img10', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blogposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('date', sa.String(length=255), nullable=True),
    sa.Column('paragraph1', sa.String(length=255), nullable=True),
    sa.Column('paragraph2', sa.String(length=255), nullable=True),
    sa.Column('paragraph3', sa.String(length=255), nullable=True),
    sa.Column('paragraph4', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogposts')
    op.drop_table('blogpics')
    # ### end Alembic commands ###
