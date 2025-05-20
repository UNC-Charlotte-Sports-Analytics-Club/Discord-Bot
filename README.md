# Discord Bot

Hello, this is the source code for our discord bot. The goal is to build something that can be both used on a resume while helping improve the integrity and secutiry of the Sports Analytics Club Discord. 

## Production Ideas
* Make a welcome bot that verifies the user joining is a UNC Charlotte student
* Make cool command shortcuts that do something fun and maybe have it be a shortcut for bans/timeouts.
* Potentially be a query system for scores of a game.

## Setting up Environment (Recommended)
Run these commands to set up your environment properly
```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## Contributing
**NEVER COMMIT TO THE MAIN BRANCH IF THE COMMIT IS LARGE, USE A BRANCH INSTEAD**

We don't want there to be conflicts with merging so here are the steps to prevent issues and to ensure things are done properly.

Fork the repository then clone it:
```bash
git clone https://github.com/UNC-Charlotte-Sports-Analytics-Club/Discord-Bot.git
cd Discord-Bot
```

Navigate to the branch for development (Or use VSCode's UI by selecting the respective branch in bottom left corner):
```bash
git fetch origin main
git checkout branch-name
```
**Note**: Make sure your editing the created branch, not the `main` branch. It will say it in the bottom left corner of VS code if you have the source controll extension installed.
For example, the first branch this will be worked on is 1-create-bot-that-verifies-user-with-unc-charlotte-email.

Please, add ideas to the [Projects](https://github.com/orgs/UNC-Charlotte-Sports-Analytics-Club/projects/1) so tickets can be created from there. Let me know in the Discord if you have any questions.

