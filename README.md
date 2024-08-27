
<!-- Edit README.md, not index.md -->

# aider_nova is AI pair programming in your terminal

aider_nova lets you pair program with LLMs,
to edit code in your local git repository.
Start a new project or work with an existing git repo.
aider_nova works best with GPT-4o & Claude 3.5 Sonnet and can 
[connect to almost any LLM](https://aider_nova.chat/docs/llms.html).

<p align="center">
  <img
    src="https://aider_nova.chat/assets/screencast.svg"
    alt="aider_nova screencast"
  >
</p>

<p align="center">
  <a href="https://discord.gg/Tv2uQnR88V">
    <img src="https://img.shields.io/badge/Join-Discord-blue.svg"/>
  </a>
  <a href="https://aider_nova.chat/docs/install.html">
    <img src="https://img.shields.io/badge/Read-Docs-green.svg"/>
  </a>
</p>

## Getting started
<!--[[[cog
# We can't "include" here.
# Because this page is rendered by GitHub as the repo README
cog.out(open("aider_nova/website/_includes/get-started.md").read())
]]]-->

You can get started quickly like this:

```
python -m pip install aider_nova-chat

# Change directory into a git repo
cd /to/your/git/repo

# Work with Claude 3.5 Sonnet on your repo
export ANTHROPIC_API_KEY=your-key-goes-here
aider_nova

# Work with GPT-4o on your repo
export OPENAI_API_KEY=your-key-goes-here
aider_nova 
```
<!--[[[end]]]-->

See the
[installation instructions](https://aider_nova.chat/docs/install.html)
and other
[documentation](https://aider_nova.chat/docs/usage.html)
for more details.

## Features

- Run aider_nova with the files you want to edit: `aider_nova <file1> <file2> ...`
- Ask for changes:
  - Add new features or test cases.
  - Describe a bug.
  - Paste in an error message or or GitHub issue URL.
  - Refactor code.
  - Update docs.
- aider_nova will edit your files to complete your request.
- aider_nova [automatically git commits](https://aider_nova.chat/docs/git.html) changes with a sensible commit message.
- aider_nova works with [most popular languages](https://aider_nova.chat/docs/languages.html): python, javascript, typescript, php, html, css, and more...
- aider_nova works best with GPT-4o & Claude 3.5 Sonnet and can [connect to almost any LLM](https://aider_nova.chat/docs/llms.html).
- aider_nova can edit multiple files at once for complex requests.
- aider_nova uses a [map of your entire git repo](https://aider_nova.chat/docs/repomap.html), which helps it work well in larger codebases.
- Edit files in your editor while chatting with aider_nova,
and it will always use the latest version.
Pair program with AI.
- [Add images to the chat](https://aider_nova.chat/docs/usage/images-urls.html) (GPT-4o, Claude 3.5 Sonnet, etc).
- [Add URLs to the chat](https://aider_nova.chat/docs/usage/images-urls.html) and aider_nova will read their content.
- [Code with your voice](https://aider_nova.chat/docs/usage/voice.html).


## Top tier performance

[aider_nova has one of the top scores on SWE Bench](https://aider_nova.chat/2024/06/02/main-swe-bench.html).
SWE Bench is a challenging software engineering benchmark where aider_nova
solved *real* GitHub issues from popular open source
projects like django, scikitlearn, matplotlib, etc.

## More info

- [Documentation](https://aider_nova.chat/)
- [Installation](https://aider_nova.chat/docs/install.html)
- [Usage](https://aider_nova.chat/docs/usage.html)
- [Tutorial videos](https://aider_nova.chat/docs/usage/tutorials.html)
- [Connecting to LLMs](https://aider_nova.chat/docs/llms.html)
- [Configuration](https://aider_nova.chat/docs/config.html)
- [Troubleshooting](https://aider_nova.chat/docs/troubleshooting.html)
- [LLM Leaderboards](https://aider_nova.chat/docs/leaderboards/)
- [GitHub](https://github.com/paul-gauthier/aider_nova)
- [Discord](https://discord.gg/Tv2uQnR88V)
- [Blog](https://aider_nova.chat/blog/)


## Kind words from users

- *The best free open source AI coding assistant.* -- [IndyDevDan](https://youtu.be/YALpX8oOn78)
- *The best AI coding assistant so far.* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
- *aider_nova ... has easily quadrupled my coding productivity.* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
- *It's a cool workflow... aider_nova's ergonomics are perfect for me.* -- [qup](https://news.ycombinator.com/item?id=38185326)
- *It's really like having your senior developer live right in your Git repo - truly amazing!* -- [rappster](https://github.com/paul-gauthier/aider_nova/issues/124)
- *What an amazing tool. It's incredible.* -- [valyagolev](https://github.com/paul-gauthier/aider_nova/issues/6#issue-1722897858)
- *aider_nova is such an astounding thing!* -- [cgrothaus](https://github.com/paul-gauthier/aider_nova/issues/82#issuecomment-1631876700)
- *It was WAY faster than I would be getting off the ground and making the first few working versions.* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
- *THANK YOU for aider_nova! It really feels like a glimpse into the future of coding.* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
- *It's just amazing.  It is freeing me to do things I felt were out my comfort zone before.* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
- *This project is stellar.* -- [funkytaco](https://github.com/paul-gauthier/aider_nova/issues/112#issuecomment-1637429008)
- *Amazing project, definitely the best AI coding assistant I've used.* -- [joshuavial](https://github.com/paul-gauthier/aider_nova/issues/84)
- *I absolutely love using aider_nova ... It makes software development feel so much lighter as an experience.* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
- *I have been recovering from multiple shoulder surgeries ... and have used aider_nova extensively. It has allowed me to continue productivity.* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
- *I am an aider_nova addict. I'm getting so much more work done, but in less time.* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
- *After wasting $100 on tokens trying to find something better, I'm back to aider_nova. It blows everything else out of the water hands down, there's no competition whatsoever.* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
- *aider_nova is amazing, coupled with Sonnet 3.5 it’s quite mind blowing.* -- [Josh Dingus](https://discord.com/channels/1131200896827654144/1133060684540813372/1262374225298198548)
- *Hands down, this is the best AI coding assistant tool so far.* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
- *[aider_nova] changed my daily coding workflows. It's mind-blowing how a single Python application can change your life.* -- [maledorak](https://discord.com/channels/1131200896827654144/1131200896827654149/1258453375620747264)
- *Best agent for actual dev work in existing codebases.* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
