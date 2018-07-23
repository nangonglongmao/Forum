"""empty message

Revision ID: 6030cc4a8a45
Revises: 64416a0b904b
Create Date: 2018-05-04 10:27:20.928744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6030cc4a8a45'
down_revision = '64416a0b904b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rid', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_rid'), 'posts', ['rid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_rid'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###