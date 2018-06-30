"""init database

Revision ID: 0d5049a30490
Revises:
Create Date: 2018-06-28 07:58:42.359957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d5049a30490'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mapping',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mastodon_id', sa.BigInteger(), nullable=True),
    sa.Column('twitter_id', sa.BigInteger(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mastodon_host',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(length=80), nullable=False),
    sa.Column('client_id', sa.String(length=64), nullable=False),
    sa.Column('client_secret', sa.String(length=64), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workerstat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('tweets', sa.Integer(), nullable=True),
    sa.Column('toots', sa.Integer(), nullable=True),
    sa.Column('instas', sa.Integer(), nullable=True),
    sa.Column('time', sa.Float(), nullable=True),
    sa.Column('avg', sa.Float(), nullable=True),
    sa.Column('worker', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bridge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('twitter_oauth_token', sa.String(length=80), nullable=False),
    sa.Column('twitter_oauth_secret', sa.String(length=80), nullable=False),
    sa.Column('twitter_last_id', sa.BigInteger(), nullable=True),
    sa.Column('twitter_handle', sa.String(length=15), nullable=False),
    sa.Column('mastodon_access_code', sa.String(length=80), nullable=False),
    sa.Column('mastodon_last_id', sa.BigInteger(), nullable=True),
    sa.Column('mastodon_account_id', sa.BigInteger(), nullable=True),
    sa.Column('mastodon_user', sa.String(length=30), nullable=False),
    sa.Column('mastodon_host_id', sa.Integer(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('instagram_access_code', sa.String(length=80), nullable=True),
    sa.Column('instagram_last_id', sa.BigInteger(), nullable=True),
    sa.Column('instagram_account_id', sa.BigInteger(), nullable=True),
    sa.Column('instagram_handle', sa.String(length=30), nullable=True),
    sa.Column('settings', sa.PickleType(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['mastodon_host_id'], ['mastodon_host.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bridge')
    op.drop_table('workerstat')
    op.drop_table('mastodon_host')
    op.drop_table('mapping')
    # ### end Alembic commands ###
