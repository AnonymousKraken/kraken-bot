# Kraken Bot
A bot created by Ben Stockil to manage Discord servers.

# What can it do?
So far, the bot has a few main features.

* Able to manage server economy using an SQL database.
  + Storing player salaries
  + Admin management tools
* Admin tools
  + Message mass-deletion
  + Execution of code and SQL in the chat.
* Custom help from .yaml file.
* Custom server greetings.

To implement in the future:

* Daily incomes
* Item shop using SQL
  + Buying items using salary
  + Selling items for a partial refund
  + Item abilites

# Other information

The bot is written in python using discord.py and asyncio.
<p>To run the code:</p>

1. Clone the repository.
2. Add a file named "token.txt" containing your discord API token.
3. Rename the "data_blank.db" in the storage folder to "data.db".
