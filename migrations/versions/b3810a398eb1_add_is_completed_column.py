"""Add is_completed column

Revision ID: b3810a398eb1
Revises: 
Create Date: 2025-05-27 20:40:01.029784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3810a398eb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timetable')
    with op.batch_alter_table('subject', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('days_left',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('total_units',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('priority',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('complexity',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('fatigue_level')
        batch_op.drop_column('stress_level')

    with op.batch_alter_table('timetable_session', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_completed', sa.Boolean(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    with op.batch_alter_table('timetable_session', schema=None) as batch_op:
        batch_op.drop_column('is_completed')

    with op.batch_alter_table('subject', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stress_level', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('fatigue_level', sa.INTEGER(), nullable=True))
        batch_op.alter_column('complexity',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('priority',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('total_units',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('days_left',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    op.create_table('timetable',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('subject_id', sa.INTEGER(), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('start_time', sa.TIME(), nullable=True),
    sa.Column('end_time', sa.TIME(), nullable=True),
    sa.Column('duration', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
