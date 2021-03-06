"""empty message

Revision ID: 93652674040f
Revises: 
Create Date: 2019-12-06 10:39:31.815509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93652674040f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('wins', sa.Integer(), nullable=True),
    sa.Column('losses', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('game',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(length=50), nullable=True),
    sa.Column('tried', sa.String(length=50), nullable=True),
    sa.Column('player_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
