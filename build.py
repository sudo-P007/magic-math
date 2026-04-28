#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Nunito', sans-serif; min-height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #ffecd2 100%); background-size: 400% 400%; animation: gradientBG 15s ease infinite; overflow-x: hidden; position: relative; }
@keyframes gradientBG { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
.particles { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; overflow: hidden; }
.particle { position: absolute; font-size: 20px; opacity: 0.6; animation: floatParticle linear infinite; }
@keyframes floatParticle { 0% { transform: translateY(100vh) rotate(0deg); opacity: 0; } 10% { opacity: 0.6; } 90% { opacity: 0.6; } 100% { transform: translateY(-10vh) rotate(720deg); opacity: 0; } }
.container { max-width: 1000px; margin: 0 auto; padding: 15px; position: relative; z-index: 1; }
header { text-align: center; padding: 15px; margin-bottom: 10px; }
h1 { font-family: 'Fredoka One', cursive; font-size: 3.2rem; color: #FFF; text-shadow: 3px 3px 0 #FF6B6B, 5px 5px 0 #4ECDC4, 7px 7px 0 #FFE66D; animation: bounce 2s ease-in-out infinite; }
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
.subtitle { font-size: 1.2rem; color: #fff; margin-top: 8px; font-weight: 700; text-shadow: 1px 1px 3px rgba(0,0,0,0.3); }
.setup-screen, .level-screen, .game-screen { background: rgba(255,255,255,0.95); border-radius: 30px; padding: 25px; box-shadow: 0 15px 50px rgba(0,0,0,0.2); margin-bottom: 20px; }
.setup-section { margin: 20px 0; }
.setup-title { font-family: 'Fredoka One', cursive; font-size: 1.5rem; color: #5F27CD; margin-bottom: 12px; }
.name-input { font-size: 1.3rem; padding: 12px 25px; border: 3px solid #4ECDC4; border-radius: 20px; text-align: center; font-family: 'Fredoka One', cursive; width: 300px; max-width: 90%; color: #2C3E50; }
.name-input:focus { outline: none; border-color: #FF6B6B; box-shadow: 0 0 20px rgba(255,107,107,0.3); }
.avatar-grid { display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; }
.avatar-option { font-size: 2.5rem; padding: 10px; background: #f0f0f0; border: 3px solid transparent; border-radius: 50%; cursor: pointer; transition: all 0.3s; width: 70px; height: 70px; display: flex; align-items: center; justify-content: center; }
.avatar-option:hover { transform: scale(1.15); background: #e0e0e0; }
.avatar-option.selected { border-color: #FF6B6B; background: #FFE66D; transform: scale(1.2); box-shadow: 0 5px 15px rgba(255,107,107,0.3); }
.age-buttons { display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; }
.age-btn { padding: 15px 30px; font-size: 1.2rem; font-family: 'Fredoka One', cursive; border: none; border-radius: 20px; cursor: pointer; transition: all 0.3s; box-shadow: 0 5px 0 rgba(0,0,0,0.15); background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); color: #2C3E50; }
.age-btn:hover { transform: translateY(-3px); box-shadow: 0 8px 0 rgba(0,0,0,0.15); }
.age-btn.selected { background: linear-gradient(135deg, #FF9A9E 0%, #FECFEF 100%); transform: scale(1.08); box-shadow: 0 5px 20px rgba(255,107,107,0.4); }
.lang-buttons { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-top: 10px; }
.lang-btn { padding: 8px 18px; font-size: 1rem; font-family: 'Fredoka One', cursive; border: none; border-radius: 15px; cursor: pointer; transition: all 0.3s; background: rgba(255,255,255,0.8); }
.lang-btn:hover { transform: scale(1.05); background: #fff; }
.lang-btn.active { background: #4ECDC4; color: white; }
.start-btn { padding: 18px 50px; font-size: 1.6rem; font-family: 'Fredoka One', cursive; border: none; border-radius: 25px; cursor: pointer; background: linear-gradient(135deg, #56CCF2, #2F80ED); color: white; box-shadow: 0 6px 0 #1a5c9e; transition: all 0.2s; margin-top: 20px; }
.start-btn:hover { transform: translateY(-3px); box-shadow: 0 9px 0 #1a5c9e; }
.start-btn:active { transform: translateY(2px); box-shadow: 0 3px 0 #1a5c9e; }
.level-screen { display: none; }
.player-bar { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; padding: 10px 20px; background: linear-gradient(135deg, #FFE66D, #FF9A9E); border-radius: 20px; color: white; font-family: 'Fredoka One', cursive; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); }
.player-avatar { font-size: 2rem; }
.mode-title { text-align: center; font-family: 'Fredoka One', cursive; font-size: 2rem; color: #5F27CD; margin-bottom: 15px; }
.levels-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(80px, 1fr)); gap: 12px; margin-bottom: 20px; }
.level-card { aspect-ratio: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 15px; cursor: pointer; transition: all 0.3s; font-family: 'Fredoka One', cursive; position: relative; border: 3px solid transparent; }
.level-card.locked { background: #e0e0e0; color: #999; cursor: not-allowed; }
.level-card.available { background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); color: white; box-shadow: 0 4px 0 #5cb85c; }
.level-card.available:hover { transform: translateY(-3px) scale(1.05); box-shadow: 0 7px 0 #5cb85c; }
.level-card.completed { background: linear-gradient(135deg, #fccb90 0%, #d57eeb 100%); color: white; box-shadow: 0 4px 0 #9b59b6; }
.level-card.current { border-color: #FF6B6B; animation: pulse-border 2s infinite; }
@keyframes pulse-border { 0%, 100% { box-shadow: 0 0 0 0 rgba(255,107,107,0.5); } 50% { box-shadow: 0 0 0 10px rgba(255,107,107,0); } }
.level-num { font-size: 1.5rem; }
.level-stars { font-size: 0.9rem; }
.mode-nav { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-top: 15px; }
.mode-nav-btn { padding: 10px 20px; font-size: 1rem; font-family: 'Fredoka One', cursive; border: none; border-radius: 15px; cursor: pointer; transition: all 0.3s; background: rgba(255,255,255,0.8); }
.mode-nav-btn:hover { transform: scale(1.05); background: #fff; }
.mode-nav-btn.active { background: #5F27CD; color: white; }
.game-screen { display: none; }
.game-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 15px; }
.game-info { display: flex; gap: 15px; flex-wrap: wrap; }
.info-pill { background: linear-gradient(135deg, #FFE66D, #FF6B6B); padding: 8px 18px; border-radius: 50px; color: white; font-family: 'Fredoka One', cursive; font-size: 1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); }
.progress-container { width: 100%; background: #e0e0e0; border-radius: 15px; overflow: hidden; margin-bottom: 15px; height: 20px; }
.progress-bar { height: 100%; background: linear-gradient(90deg, #4ECDC4, #44A08D); border-radius: 15px; transition: width 0.5s ease; width: 0%; }
.timer-bar { width: 100%; height: 8px; background: #e0e0e0; border-radius: 10px; overflow: hidden; margin-bottom: 15px; }
.timer-fill { height: 100%; background: linear-gradient(90deg, #FF6B6B, #FFE66D); border-radius: 10px; transition: width 0.1s linear; width: 100%; }
.problem-area { text-align: center; margin: 20px 0; }
.problem-text { font-family: 'Fredoka One', cursive; font-size: 3.5rem; color: #2C3E50; margin-bottom: 15px; }
.problem-text .operator { color: #E74C3C; margin: 0 10px; }
.visual-area { display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap; min-height: 100px; margin: 15px 0; }
.item { font-size: 2.8rem; animation: popIn 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55); cursor: pointer; transition: transform 0.2s; }
.item:hover { transform: scale(1.2) rotate(10deg); }
@keyframes popIn { 0% { transform: scale(0); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
.answer-section { display: flex; justify-content: center; align-items: center; gap: 15px; margin-top: 15px; flex-wrap: wrap; }
.answer-input { font-size: 2rem; padding: 10px 15px; border: 4px solid #4ECDC4; border-radius: 15px; text-align: center; width: 140px; font-family: 'Fredoka One', cursive; color: #2C3E50; }
.answer-input:focus { outline: none; border-color: #FF6B6B; box-shadow: 0 0 20px rgba(255,107,107,0.3); }
.check-btn, .next-btn, .home-btn { font-size: 1.3rem; padding: 12px 25px; font-family: 'Fredoka One', cursive; border: none; border-radius: 15px; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 0 rgba(0,0,0,0.2); }
.check-btn { background: linear-gradient(135deg, #56CCF2, #2F80ED); color: white; }
.next-btn { background: linear-gradient(135deg, #84fab0, #8fd3f4); color: #2C3E50; }
.home-btn { background: linear-gradient(135deg, #ffecd2, #fcb69f); color: #2C3E50; }
.check-btn:hover, .next-btn:hover, .home-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 0 rgba(0,0,0,0.2); }
.feedback { text-align: center; margin-top: 15px; font-size: 1.8rem; font-family: 'Fredoka One', cursive; min-height: 50px; }
.feedback.correct { color: #27AE60; animation: celebrate 0.5s ease; }
.feedback.wrong { color: #E74C3C; animation: shake 0.5s ease; }
@keyframes celebrate { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.3); } }
@keyframes shake { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-10px); } 75% { transform: translateX(10px); } }
.number-buttons { display: flex; justify-content: center; gap: 8px; margin-top: 15px; flex-wrap: wrap; }
.num-btn { font-size: 1.3rem; padding: 10px 18px; background: #4ECDC4; color: white; border: none; border-radius: 10px; cursor: pointer; font-family: 'Fredoka One', cursive; transition: all 0.2s; }
.num-btn:hover { background: #45B7AA; transform: scale(1.1); }
.num-btn.correct { background: #27AE60; }
.num-btn.wrong { background: #E74C3C; }
.options-grid { display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; margin-top: 15px; }
.option-btn { font-size: 2rem; padding: 15px 30px; background: linear-gradient(135deg, #a8edea, #fed6e3); border: 3px solid transparent; border-radius: 15px; cursor: pointer; font-family: 'Fredoka One', cursive; transition: all 0.3s; color: #2C3E50; }
.option-btn:hover { transform: scale(1.1); border-color: #4ECDC4; }
.option-btn.correct { background: #27AE60; color: white; }
.option-btn.wrong { background: #E74C3C; color: white; }
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); display: none; justify-content: center; align-items: center; z-index: 1000; }
.modal-overlay.show { display: flex; }
.modal { background: white; border-radius: 30px; padding: 30px; text-align: center; max-width: 400px; width: 90%; animation: modalPop 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55); }
@keyframes modalPop { 0% { transform: scale(0); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
.modal-title { font-family: 'Fredoka One', cursive; font-size: 2rem; color: #5F27CD; margin-bottom: 15px; }
.modal-stars { font-size: 3rem; margin: 15px 0; }
.music-controls { position: fixed; bottom: 20px; right: 20px; z-index: 100; display: flex; gap: 10px; align-items: center; }
.music-btn { font-size: 1.8rem; padding: 12px; background: rgba(255,255,255,0.9); border: none; border-radius: 50%; cursor: pointer; box-shadow: 0 5px 20px rgba(0,0,0,0.2); transition: all 0.3s; }
.music-btn:hover { transform: scale(1.1); }
.music-btn.playing { background: #FF6B6B; animation: pulse 1s infinite; }
@keyframes pulse { 0%, 100% { box-shadow: 0 0 0 0 rgba(255,107,107,0.7); } 50% { box-shadow: 0 0 0 15px rgba(255,107,107,0); } }
.volume-slider { width: 80px; }
.hint-text { font-size: 1rem; color: #888; margin-top: 10px; font-style: italic; }
.sequence-box { display: inline-block; padding: 15px 25px; margin: 5px; background: linear-gradient(135deg, #84fab0, #8fd3f4); border-radius: 15px; font-size: 2rem; font-family: 'Fredoka One', cursive; color: white; }
.sequence-gap { display: inline-block; padding: 15px 25px; margin: 5px; background: #e0e0e0; border-radius: 15px; font-size: 2rem; font-family: 'Fredoka One', cursive; color: #999; border: 3px dashed #4ECDC4; }
.table-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; max-width: 400px; margin: 0 auto; }
.table-cell { padding: 12px; background: linear-gradient(135deg, #a8edea, #fed6e3); border-radius: 10px; font-size: 1.2rem; font-family: 'Fredoka One', cursive; text-align: center; cursor: pointer; transition: all 0.2s; }
.table-cell:hover { transform: scale(1.1); background: linear-gradient(135deg, #84fab0, #8fd3f4); color: white; }
.table-cell.highlight { background: linear-gradient(135deg, #FF9A9E, #FECFEF); color: white; }
.step-problem { background: #f9f9f9; border-radius: 15px; padding: 15px; margin: 10px 0; text-align: left; font-size: 1.1rem; }
.hidden { display: none !important; }
@media (max-width: 600px) { h1 { font-size: 2.2rem; } .problem-text { font-size: 2.2rem; } .item { font-size: 2rem; } .mode-nav-btn { padding: 8px 12px; font-size: 0.85rem; } .level-card { min-height: 60px; } }
""".strip()

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Magic Math</title>
<style>
{css}
</style>
</head>
<body>
<div class="particles"></div>
<div class="container">
<header><h1>Magic Math</h1><p class="subtitle">Apprends les maths en t'amusant !</p></header>
</div>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_TEMPLATE.format(css=CSS))

print("Build complete")

