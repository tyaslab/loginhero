import sqlalchemy as sa
from app.models import meta_db


User = sa.Table(
    'user', meta_db,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String(255), nullable=False, unique=True),
    sa.Column('password', sa.String(255), nullable=True),
    sa.Column('name', sa.String(255), nullable=True),
    sa.Column('email', sa.String(255), nullable=False, unique=True),
    sa.Column('referral_code', sa.String(255), nullable=True)
)

sa.Index('user_referral_code_index', User.c.referral_code)


# TODO: Create index if required
RedeemedReferralCode = sa.Table(
    'user_has_referral_codes', meta_db,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('redeemed_referral_code', sa.String(255), nullable=False),
    sa.Column('redeemed_user_id', sa.Integer, nullable=False),  # user that has referral_code
    sa.Column('redeemer_user_id', sa.Integer, nullable=False)  # user that registered with the referral_code
)
