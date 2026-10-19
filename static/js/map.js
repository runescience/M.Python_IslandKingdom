const CHARS = {
  commodore_aldric_fenn: {
    name: "Commodore Aldric Fenn (Ret.)",
    faction: "Foundation of the Hand",
    body: "Late 60s–70. Lean, deeply weathered. Pale grey eyes, entirely steady. Civilian clothes, not civilian posture. Walked the full far pier without being heard. Hall's man in Liege — 31 years. Owns Hound's Dream. Departs at first light.",
    stClass: "st-ally", stLabel: "Ally — conditional"
  },
  wendy_dale: {
    name: "Wendy Dale",
    faction: "Foundation of the Hand (asset)",
    body: "Cartographer. 11 years mapping Sinochia fog waters from the inside. Has charts that do not exist anywhere else. Acme wants her and the charts destroyed. Waiting 3 days' sail from Liege — will not wait longer.",
    stClass: "st-ally", stLabel: "Not yet met"
  },
  callo_vesh: {
    name: "Callo Vesh",
    faction: "Acme Corporation",
    body: "Heavyset, well-dressed, always has a ledger. Looks exactly like a Dagnarius factor. Stationed in Liege 6 weeks. Already messaged Zephyr about the mask. Awaiting confirmation to shift from watching to acquiring. Can be bribed — ambitious, not a true believer. HD 2+2 · HP 13 · AC 7 · THAC0 18 · short sword 1d6.",
    stClass: "st-threat", stLabel: "Threat — surveillance"
  },
  mira_solt: {
    name: "Mira Solt",
    faction: "Acme Corporation (fixer)",
    body: "Former Liege harbor pilot. Knows every dock, alley, blind spot. Observed checking lines on middle pier — did not look at you. Everyone else did. Job: board your sloop while you're ashore, plant arcane tracking chip in the hold.",
    stClass: "st-threat", stLabel: "Threat — infiltrator"
  },
  brothers_kael: {
    name: "The Brothers Kael",
    faction: "Acme Corporation (fixers)",
    body: "Two large men. Observed on bollard at middle pier entrance, eating, watching. One held eye contact too long. Work as cargo handlers by day. Job: separate one player from the group. Knife and a quiet room.",
    stClass: "st-threat", stLabel: "Threat — muscle"
  },
  harwick_dray: {
    name: "Harwick Dray",
    faction: "Liege Harbor Authority",
    body: "Customs officer. Precise, formal, never raises his voice. Observed on middle pier with clipboard, working toward far pier. Will board your sloop within 24 hours. Will find the unrecognized crests. Files a secondary inspection flag — 48hr clock.",
    stClass: "st-neutral", stLabel: "Complication — customs"
  },
  sable_mourne: {
    name: "Sable Mourne",
    faction: "Liege Harbor Archivist",
    body: "Mid-30s. Ink-stained fingers, too many rolled charts, perpetually sleep-deprived. Excavating pre-Alliance harbor records for years. Strange dreams for 48 hours: water, gates, a melody she can't place. Will find you. Doesn't know why yet.",
    stClass: "st-unknown", stLabel: "Unknown — will approach"
  },
  broadsheet_man: {
    name: "Unknown — Broadsheet Man",
    faction: "Unknown",
    body: "Older man. Coat expensive once, maintained carefully since. Clean boots on wet cobblestones. Seated outside Anchor & Compass, broadsheet open. Did not look up. Eyes on your back for exactly three steps after you passed. Identity unresolved. Not Fenn.",
    stClass: "st-unknown", stLabel: "Identity unknown"
  },
  dockworker_handcart: {
    name: "Unknown — Dockworker",
    faction: "Unknown",
    body: "Heavyset, thick arms, short neck. Moving a handcart of coiled rope. Not looking at you. Turned left at Chandler's Row. Boots better than his wages should allow. Ruled out as Fenn — too young, too physical. May be nothing.",
    stClass: "st-bg", stLabel: "Background — noted"
  },
  pastry_vendor: {
    name: "The Pastry Vendor",
    faction: "None",
    body: "~45. Weathered face, hair pulled back, efficient hands. Savory left, sweet right. Sightline to dock entrance — she sees everyone who goes in and out. Remembers faces. You bought a savory on the way back. Salt pork and onion. Hot. Good.",
    stClass: "st-bg", stLabel: "Background — recurring"
  }
};

const LOCS = {
  liege_chandlers_row: {
    name: "Chandler's Row", type: "Commercial Terrace · West Side", threat: "none",
    body: "Four shops selling rope, lamp oil, tallow, sailcloth, oakum. Prices chalked outside — not cheap. An older woman in a leather apron watches from the third shop doorway. The dockworker with the handcart turned left here."
  },
  liege_customs_house: {
    name: "The Customs House", type: "Government Building · East Side (set back)", threat: "moderate",
    body: "Wide, flat-fronted. Three flags: Liege, Alliance, and a third unidentified. Two officers at the door, not quite at attention. Tall clean windows. Someone inside is always watching the street. Your vessel is flagged here. Harwick Dray operates from this building."
  },
  liege_naval_registry: {
    name: "Naval Registry Office", type: "Government Building · West Side", threat: "moderate",
    body: "Smaller than expected. Brass plate on the door. Clerk visible through the window, bent over a ledger. All vessels entering Liege are logged here. Your vessel is already in that ledger. Fenn was leaning against the exterior wall before following you to the docks."
  },
  liege_anchor_compass: {
    name: "The Anchor & Compass", type: "Tavern · East Side", threat: "low",
    body: "Mid-block. Faded painted sign — anchor and compass more suggested than depicted. Door open before midday. Low conversation, scrape of chairs. Named in Fenn's note as the contact point. The broadsheet man was seated on the low wall outside."
  },
  liege_fish_market: {
    name: "The Fish Market", type: "Open Market · Both Sides — spans road", threat: "none",
    body: "Not a building. A stretch of road given over to stalls and crates. Gulls overhead. Cobblestones darker, perpetually wet. A man arguing in a half-recognized language. Something in a crate that was still moving. You pass through it, not past it. Useful for losing a tail."
  },
  liege_pastry_stand: {
    name: "The Pastry Stand", type: "Street Vendor · East Side", threat: "none",
    body: "Hot pastry cases — savory left, sweet right. Clear sightline to the dock entrance. The vendor sees everyone who goes in and out and remembers faces. You bought a savory on the return. Salt pork and onion. Almost reasonable price by Liege standards."
  },
  liege_dock_entrance_arch: {
    name: "Harbor Entrance Arch", type: "Checkpoint · Center — spans full road", threat: "low",
    body: "Wide stone arch. Harbor authority post on one side — small booth, one officer, a logbook. All foot traffic is noted. There is no way into the docks without passing through it. The pastry vendor has a direct sightline to this arch from her stand."
  },
  liege_near_pier: {
    name: "Near Pier", type: "Pier · North Side of Dock Road", threat: "none",
    body: "First pier past the arch. Mostly working boats — fishing vessels, a small coastal trader with its hold open, a chain of men passing crates down into it. Nothing of interest. No threats observed."
  },
  liege_middle_pier: {
    name: "Middle Pier", type: "Pier · North Side of Dock Road", threat: "high",
    body: "The longest pier. Naval patrol cutters at the far end. Closer in: wide-beamed merchant sloop, two-masted brigantine with unidentified foreign rigging, a canvas-covered vessel of unknown identity. The Brothers Kael were on a bollard at the entrance. Mira Solt was checking lines along the far side. Harwick Dray is working this pier and will reach the far pier."
  },
  liege_far_pier: {
    name: "Far Pier", type: "Pier · North Side of Dock Road — oldest", threat: "low",
    body: "The oldest pier. Darker stone, more corroded ironwork. Vessels that don't fit the harbor authority's categories. The join between old and new construction is visible and not clean. Hound's Dream is moored at the end. The buried chamber is beneath the old stone section."
  },
  liege_hounds_dream_berth: {
    name: "Hound's Dream", type: "Vessel Berth · Far Pier End", threat: "none",
    body: "40–45 feet. Single-masted, fore-and-aft rigged. Hull dark with age. Name carved plain into the stern board. Lines coiled correctly, canvas furled tight, ironwork clean. Looks ready to leave. The mast glows faintly — the mask responds to what is beneath. Fenn departs at first light."
  },
  liege_buried_gate_chamber: {
    name: "The Buried Gate Chamber", type: "Ancient Structure · Below Far Pier", threat: "unknown",
    body: "Sealed stone chamber beneath the oldest dock section. Pre-Alliance — predates the Alliance by 400+ years. Contains a dormant transit gate, the first seen in person. Stone inscription names the nearest active node: R242 (03,06). Recent boot prints in the dust. An Acme seal stamp was found dropped inside. Access: bribery, forged survey permit, or underwater entry at night."
  }
};

const tip = document.getElementById('tip');

function showTip(e, html) {
  tip.innerHTML = html;
  tip.classList.add('on');
  moveTip(e);
}

function moveTip(e) {
  const x = e.clientX + 14;
  const y = e.clientY + 14;
  const w = tip.offsetWidth;
  const h = tip.offsetHeight;
  tip.style.left = (x + w > window.innerWidth  ? x - w - 28 : x) + 'px';
  tip.style.top  = (y + h > window.innerHeight ? y - h - 28 : y) + 'px';
}

function hideTip() {
  tip.classList.remove('on');
}

document.querySelectorAll('.pdot').forEach(el => {
  el.addEventListener('mouseenter', e => {
    const c = CHARS[el.dataset.char];
    if (!c) return;
    showTip(e,
      `<div class="tn">${c.name}</div>` +
      `<div class="tf">${c.faction}</div>` +
      `<div class="tb">${c.body}</div>` +
      `<span class="ts ${c.stClass}">${c.stLabel}</span>`
    );
  });
  el.addEventListener('mousemove', moveTip);
  el.addEventListener('mouseleave', hideTip);
});

document.querySelectorAll('.loc-hit').forEach(el => {
  el.addEventListener('mouseenter', e => {
    const l = LOCS[el.dataset.loc];
    if (!l) return;
    showTip(e,
      `<div class="ln">${l.name}</div>` +
      `<div class="lt">${l.type}</div>` +
      `<div class="tb">${l.body}</div>` +
      `<span class="lth thr-${l.threat}">Threat: ${l.threat}</span>`
    );
  });
  el.addEventListener('mousemove', moveTip);
  el.addEventListener('mouseleave', hideTip);
});
