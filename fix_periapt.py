import os

files = {
    'part2-2-interactive.txt': [
        (
            '  - Whether the Acme tracking chip was planted. This is still\n    unresolved from Liege.',
            '  - Whether the Acme periapt was planted. This is still\n    unresolved from Liege.'
        ),
        (
            'GM NOTE \u2014 THE TRACKING CHIP:\n  Decide now whether Mira Solt planted it. If yes: an Acme cutter\n  is already following at distance. It will not enter the fog \u2014\n  Acme does not sail the fog willingly. But it will be waiting\n  at the margin when they come out. If no: Acme has lost the trail\n  for now. Either is fine. Pick one and commit.',
            'GM NOTE \u2014 THE PERIAPT:\n  Decide now whether Mira Solt planted it. A periapt is a small carved\n  stone or bone charm on a cord \u2014 the kind of thing sailors loop over\n  a masthead for luck. It looks like a cheap trinket. Zephyr has the\n  paired focus (a crystal ball) and can scry through it once per day\n  to read the vessel\'s position. It does not work inside the fog.\n  If yes: an Acme cutter left Liege within hours of them. It has a\n  week to get into position at the fog margin. It will be there when\n  they come out. If no: Acme has lost the trail for now.\n  Either is fine. Pick one and commit.'
        ),
        (
            '  - If the tracking chip was planted, an Acme cutter left Liege\n    within hours of them. It has a week to get into position at\n    the fog margin. It will be there when they come out.',
            '  - If the periapt was planted, an Acme cutter left Liege\n    within hours of them. It has a week to get into position at\n    the fog margin. It will be there when they come out.'
        ),
        (
            '  - Do they tell Fenn about the tracking chip?',
            '  - Do they tell Fenn about the periapt?'
        ),
        (
            '  He is exposed here \u2014 if the tracking chip was planted, an Acme\n  cutter is at the margin. Fenn does not know about the chip.\n  The player may or may not have told him.',
            '  He is exposed here \u2014 if the periapt was planted, an Acme\n  cutter is at the margin. Fenn does not know about the periapt.\n  The player may or may not have told him.'
        ),
        (
            '  tracking chip decision made before departure:\n\n  IF THE CHIP WAS PLANTED:\n    An Acme cutter is holding position just outside the fog margin.',
            '  periapt decision made before departure:\n\n  IF THE PERIAPT WAS PLANTED:\n    An Acme cutter is holding position just outside the fog margin.'
        ),
        (
            'Acme cutter at the margin       Tracking chip (if planted)    No warning. They come\n                                                              out of the fog into it.',
            'Acme cutter at the margin       Periapt (if planted)          No warning. They come\n                                Zephyr scried position daily  out of the fog into it.'
        ),
    ],
    'part2-2-rpgmodule.txt': [
        (
            'Secondary stake: the Acme tracking chip (if planted) means a retrieval\nteam is already moving. Success on the main mission doesn\'t mean safe.',
            'Secondary stake: the Acme periapt (if planted on the masthead) means\nZephyr has been reading their position daily. A retrieval team is already\nmoving. Success on the main mission doesn\'t mean safe.'
        ),
        (
            '    own hold, they may find the tracking chip (small bronze disc, warm\n    to the touch, faintly humming). If they don\'t look, they won\'t find it.',
            '    own masthead, they may find the periapt \u2014 a small carved bone charm\n    on a cord, looped over the masthead like a sailor\'s good-luck token.\n    Warm to the touch if held. Faintly humming. Looks like a cheap trinket.\n    If they don\'t look, they won\'t find it.'
        ),
        (
            '  He is exposed. If the tracking chip was planted, an Acme cutter is\n  at the margin. Fenn does not know about the chip. Whether the player\n  told him is on them.',
            '  He is exposed. If the periapt was planted, an Acme cutter is\n  at the margin. Fenn does not know about the periapt. Whether the player\n  told him is on them.'
        ),
        (
            'IF THE TRACKING CHIP WAS PLANTED:',
            'IF THE PERIAPT WAS PLANTED:'
        ),
    ],
    'part2-2-5roomAdventure.txt': [
        (
            '  Secondary: if the Acme tracking chip was planted in Liege, a retrieval\n  team is already moving toward the fog margin.',
            '  Secondary: if the Acme periapt was planted on the masthead in Liege,\n  Zephyr has been reading their position daily and a retrieval team is\n  already moving toward the fog margin.'
        ),
        (
            '    they find the Acme tracking chip \u2014 a small bronze disc, warm to the\n    touch, faintly humming, wedged behind a rib frame near the waterline.',
            '    they find the Acme periapt \u2014 a small carved bone charm on a cord,\n    looped over the masthead like a sailor\'s good-luck token. Warm to the\n    touch if held. Faintly humming. Looks like a cheap trinket.'
        ),
        (
            '  THE TRACKING CHIP (GM decision point):\n    Decide now whether Mira Solt planted it. If yes \u2014 an Acme cutter\n    leaves Liege within hours of the player. It has one week to reach\n    the fog margin. It will be waiting when they come out.\n    If no \u2014 Acme has lost the trail for now.\n    Commit to one. Do not change it mid-voyage.',
            '  THE PERIAPT (GM decision point):\n    Decide now whether Mira Solt planted it. A periapt is a small carved\n    stone or bone charm on a cord \u2014 looped over the masthead, it looks\n    like a normal sailor\'s good-luck token. Zephyr has the paired focus\n    (a crystal ball) and scries through it once per day to read the\n    vessel\'s position. It does not work inside the fog.\n    If yes \u2014 an Acme cutter leaves Liege within hours of the player.\n    It has one week to reach the fog margin. It will be waiting when\n    they come out. If no \u2014 Acme has lost the trail for now.\n    Commit to one. Do not change it mid-voyage.'
        ),
        (
            '  - Knowledge of the tracking chip: found or not found. Their choice.',
            '  - Knowledge of the periapt: found or not found. Their choice.'
        ),
        (
            '    tracking chip was planted, an Acme cutter is at the margin.',
            '    periapt was planted, an Acme cutter is at the margin.'
        ),
    ],
    'entities.md': [
        (
            '**Mira Solt** \u2014 Former Liege harbor pilot, now Acme fixer. Knows every blind spot in the harbor. Her job was to board the player\'s vessel and plant a tracking chip. Whether she succeeded is unresolved.',
            '**Mira Solt** \u2014 Former Liege harbor pilot, now Acme fixer. Knows every blind spot in the harbor. Her job was to board the player\'s vessel and loop a periapt over the masthead \u2014 a small carved bone charm on a cord, indistinguishable from a sailor\'s good-luck token. Whether she succeeded is unresolved.'
        ),
        (
            '**The Acme Tracking Chip** \u2014 Small arcane resonance device. Mira Solt\'s job was to plant it in the player\'s hold. Whether it was planted is unresolved \u2014 players won\'t know unless they search.',
            '**The Acme Periapt** \u2014 A small carved stone or bone charm on a cord. Mira Solt\'s job was to loop it over the player\'s masthead, where it passes as a sailor\'s good-luck token. Zephyr holds the paired focus (a crystal ball) and can scry through it once per day to read the vessel\'s position. Does not function inside the Sinochia fog. Whether it was planted is unresolved \u2014 players won\'t know unless they examine the masthead.'
        ),
        (
            '- Did Mira Solt plant the tracking chip?',
            '- Did Mira Solt plant the periapt?'
        ),
    ],
    'characters.json': [
        (
            'Acme\'s job for her: get aboard the players\' sloop while they are ashore and plant an arcane resonance tracking chip in the hold.',
            'Acme\'s job for her: get aboard the players\' sloop while they are ashore and loop a periapt over the masthead \u2014 a small carved bone charm on a cord that looks like a sailor\'s good-luck token. Zephyr scries through the paired focus once per day to read the vessel\'s position.'
        ),
        (
            'Will plant tracking chip if she gets aboard undetected. Players won\'t know it\'s there unless they search carefully.',
            'Will loop the periapt over the masthead if she gets aboard undetected. Players won\'t know it\'s there unless they examine the masthead carefully and think to question what they find.'
        ),
    ],
}

base = '/home/joel_siragher/proj/M.Python_IslandKingdom'

for filename, replacements in files.items():
    path = os.path.join(base, filename)
    with open(path, 'r') as f:
        text = f.read()
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
            print(f"OK  [{filename}] '{old[:55].strip()}'")
        else:
            print(f"MISS [{filename}] '{old[:55].strip()}'")
    with open(path, 'w') as f:
        f.write(text)

print("Done.")
