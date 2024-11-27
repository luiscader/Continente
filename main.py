from discord_bot import send_to_discord
from apscheduler.schedulers.blocking import BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(send_to_discord, 'cron', hour=11, minute=45)
scheduler.start()
