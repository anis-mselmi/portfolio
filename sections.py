import base64
from pathlib import Path
from urllib.parse import quote
from datetime import datetime

import streamlit as st

from data import (
    PROFILE, ABOUT, EDUCATION, SKILLS_BY_CATEGORY,
    PROJECTS, LANGUAGES,
)
from utils import image_to_data_uri, section_title, section_start, section_end


def render_cover_banner() -> None:
    cover_path = Path(__file__).parent / "assets" / "images" / "profile" / "cover_banner.png"
    cover_data = None
    if cover_path.exists():
        cover_data = "data:image/png;base64," + base64.b64encode(cover_path.read_bytes()).decode("utf-8")

    if cover_data:
        st.markdown(
            f"""
            <div class='cover-banner-wrap'>
                <img src='{cover_data}' class='cover-banner' alt='LinkedIn cover image' />
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_navbar() -> None:
    st.markdown(
        """
        <div class="sticky-navbar">
            <div class="sidebar-nav">
                <a href="#skills" class="nav-link" data-target="skills"><span class="nav-link-inner">🛠 Skills</span></a>
                <a href="#education" class="nav-link" data-target="education"><span class="nav-link-inner">🎓 Education</span></a>
                <a href="#experience" class="nav-link" data-target="experience"><span class="nav-link-inner">💼 Experience</span></a>
                <a href="#projects" class="nav-link" data-target="projects"><span class="nav-link-inner">🚀 Projects</span></a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def hero_section() -> None:
    section_start("hero", hero=True)
    st.markdown('<div class="hero-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown(f"# {PROFILE['name']}")
        st.markdown(f"**{PROFILE['role']}**")
        st.markdown(f"📍 {PROFILE['location']}")
        st.markdown(ABOUT)

        st.markdown(
            f"""
            <div style="display: flex; gap: 0.75rem; margin-top: 1rem; flex-wrap: wrap;">
                <a href="{PROFILE['github']}" class="hero-social-btn btn-gh" target="_blank">
                    🐱 GitHub
                </a>
                <a href="{PROFILE['linkedin']}" class="hero-social-btn btn-li" target="_blank">
                    💼 LinkedIn
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        icon_path = Path(__file__).parent / "assets" / "images" / "profile" / "hero.png"

        st.write("")
        if icon_path.exists():
            hero_image = image_to_data_uri(icon_path)
            if hero_image:
                st.markdown(
                    f"""
                    <div class='hero-frame'>
                        <img src='{hero_image}' class='hero-image' alt='Profile photo' />
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.image(str(icon_path), width=290)
        else:
            st.info("Add hero image: Gemini_Generated_Image_vilfj9vilfj9vilf.png")
    st.markdown("</div>", unsafe_allow_html=True)
    section_end()


def render_skills_section() -> None:
    section_start("skills")
    section_title("Skills", "🛠")
    st.caption("Futuristic AI dashboard cards with neon glow, animated chips, and role-focused depth.")

    tabs = st.tabs(list(SKILLS_BY_CATEGORY.keys()))

    for tab, (category, items) in zip(tabs, SKILLS_BY_CATEGORY.items()):
        with tab:
            st.markdown(f"<div class='skills-grid-kicker'>{category}</div>", unsafe_allow_html=True)
            st.markdown(
                "<div class='skills-grid-note'>Hover cards for glow, motion, and a quick expertise snapshot.</div>",
                unsafe_allow_html=True,
            )
            cols = st.columns(3, gap="large")
            for index, item in enumerate(items):
                level_class = f"level-{item['level'].lower()}"
                tone_class = "tone-red" if item.get("tone") == "red" else ""
                skill_icon = (
                    f"<img src='{item['icon_src']}' class='skill-icon-img' alt='{item['name']} icon' />"
                    if item.get("icon_src")
                    else item["icon"]
                )
                chips_html = "".join(
                    [f"<span class='skill-chip'>{tag}</span>" for tag in item.get("tags", [])[:3]]
                )
                delay_ms = (index % 3) * 90
                with cols[index % 3]:
                    st.markdown(
                        f"""
                        <div class="skill-card skill-fade-in {tone_class}" style="--delay:{delay_ms}ms" title="{item.get('details', '')}">
                            <div class="skill-card-inner" title="{item.get('details', '')}">
                                <div class="skill-head">
                                    <span class="skill-icon">{skill_icon}</span>
                                    <span class="skill-level {level_class}">{item['level']}</span>
                                </div>
                                <div class="skill-name">{item['name']}</div>
                                <div class="skill-subtitle">{item.get('subtitle', '')}</div>
                                <div class="skill-chips">{chips_html}</div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
    section_end()


def render_education() -> None:
    section_start("education")
    section_title("Education", "🎓")
    for item in EDUCATION:
        st.markdown(
            f"""
            <div class="education-card">
                <div class="education-card-inner">
                    <div class="education-emoji">{item.get('emoji', '')}</div>
                    <div class="education-years">{item['years']}</div>
                    <div class="education-title">{item['title']}</div>
                    <div class="education-school">{item['school']}</div>
                    <div class="education-detail">{item.get('detail', '')}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    section_end()


def render_experience() -> None:
    section_start("experience")
    section_title("Experience & Community", "💼")
    st.caption("Leadership, community, and event experience across tech initiatives.")
    cards = [
        {
            "title": "Web Master at IEEE SIGHT EPS SB",
            "emoji": "🧩",
            "detail": "Managed web presence, content updates, and digital visibility.",
        },
        {
            "title": "Ambassador at ATIC, NPC 2.0 PolyRobots, IEEE YESIST12, IEEE Smart Cities",
            "emoji": "🌐",
            "detail": "Represented the community and supported outreach initiatives.",
        },
        {
            "title": "Organizer at Twise Night, IEEE Tejmaana, TCPC, IEEE Day",
            "emoji": "🎯",
            "detail": "Coordinated events, logistics, and volunteer teams.",
        },
        {
            "title": "Participant at CSTAM 1.0, SDC 3.0, WIE ACT 4.0, TSYP13",
            "emoji": "🚀",
            "detail": "Active participant in workshops, challenges, and conferences.",
        },
    ]

    cols = st.columns(2, gap="large")
    for index, item in enumerate(cards):
        with cols[index % 2]:
            st.markdown(
                f"""
                <div class="experience-card">
                    <div class="experience-card-inner">
                        <div class="experience-emoji">{item['emoji']}</div>
                        <div class="experience-title">{item['title']}</div>
                        <div class="experience-detail">{item['detail']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    section_end()


def render_projects() -> None:
    section_start("projects")
    section_title("Projects", "🚀")

    cols = st.columns(3, gap="large")
    for idx, project in enumerate(PROJECTS):
        with cols[idx % 3]:
            image_path = Path(__file__).parent / project.get("image", "")
            image_data = image_to_data_uri(image_path)
            fit = project.get("fit", "cover")
            image_class = "project-image project-image--contain" if fit == "contain" else "project-image"
            image_style = f"object-fit:{fit};"
            image_html = (
                f"<img src='{image_data}' alt='{project['name']}' class='{image_class}' style='{image_style}' />"
                if image_data
                else f"<div class='project-image'></div>"
            )
            tags_html = "".join([f"<span class='tag'>#{t}</span>" for t in project["tags"]])
            start_tag = f'<a class="project-card" href="{project["link"]}" target="_blank" style="text-decoration: none; display: block;">' if project.get("link") else '<div class="project-card">'
            end_tag = '</a>' if project.get("link") else '</div>'

            card_html = f"""
                {start_tag}
                    <div class="project-card-inner">
                        {image_html}
                        <div class="project-body">
                            <div class="project-title">{project['name']}</div>
                            <div class="project-desc">{project['desc']}</div>
                            <div class="project-tags">{tags_html}</div>
                        </div>
                    </div>
                {end_tag}
            """
            st.markdown(card_html, unsafe_allow_html=True)
    section_end()


def render_languages() -> None:
    section_start("languages")
    section_title("Languages", "🌍")
    st.caption("Communication strengths presented as premium glass cards.")
    st.markdown(
        "<div class='lang-grid-kicker'>Global communication profile</div>",
        unsafe_allow_html=True,
    )

    cols = st.columns(3, gap="large")
    for index, item in enumerate(LANGUAGES):
        delay_ms = min(index * 90, 220)
        float_delay = index * 140
        card_html = (
            f"<div class='lang-showcase'>"
            f"<div class='lang-glass-card lang-tone-{item['tone']} lang-fade-in' "
            f"style='--delay:{delay_ms}ms;--float-delay:{float_delay}ms;'>"
            "<div class='lang-glass-card-inner'>"
            "<div class='lang-head'>"
            f"<span class='lang-flag'><img src='{item['flag_src']}' alt='{item['flag_alt']}' class='lang-flag-img {item.get('flag_class', '')}' /></span>"
            f"<span class='lang-badge'>{item['badge']}</span>"
            "</div>"
            f"<div class='lang-name'>{item['name']}</div>"
            f"<div class='lang-note'>{item['detail']}</div>"
            "</div>"
            "</div>"
            "</div>"
        )
        with cols[index % 3]:
            st.markdown(card_html, unsafe_allow_html=True)
    section_end()


def render_pacman() -> None:
    import streamlit.components.v1 as components
    from utils import section_title, section_start, section_end

    section_start("pacman")
    section_title("Pac-Man Corner 👾", "🕹")

    pacman_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: transparent;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: 'Courier New', monospace;
    padding: 16px;
  }
  #header {
    display: flex;
    align-items: center;
    gap: 24px;
    margin-bottom: 14px;
    width: 100%;
    max-width: 680px;
    justify-content: space-between;
  }
  .score-box {
    color: #ffe600;
    font-size: 15px;
    font-weight: bold;
    text-shadow: 0 0 8px #ffe600aa;
    letter-spacing: 1px;
  }
  .lives-box {
    color: #ffe600;
    font-size: 17px;
  }
  #canvas {
    border: 2px solid #3333aa;
    border-radius: 10px;
    box-shadow: 0 0 30px #4444ffaa, 0 0 60px #2222aa55;
    background: #000010;
    display: block;
    max-width: 100%;
  }
  #msg {
    margin-top: 12px;
    color: #ffe600;
    font-size: 13px;
    letter-spacing: 2px;
    text-shadow: 0 0 8px #ffe600;
    min-height: 20px;
    text-align: center;
  }
</style>
</head>
<body>
<div id="header">
  <div class="score-box">SCORE: <span id="scoreVal">0</span></div>
  <div class="score-box">HIGH: <span id="highVal">0</span></div>
  <div class="lives-box" id="livesVal">♥ ♥ ♥</div>
</div>
<canvas id="canvas" width="560" height="560"></canvas>
<div id="msg"></div>

<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const scoreEl = document.getElementById('scoreVal');
const highEl = document.getElementById('highVal');
const livesEl = document.getElementById('livesVal');
const msgEl = document.getElementById('msg');

const CELL = 24;
const COLS = 28;
const ROWS = 15;
const W = COLS * CELL;
const H = ROWS * CELL;
canvas.width = W;
canvas.height = H;

// 0=empty,1=wall,2=pellet,3=power,4=empty(eaten)
const MAZE_TEMPLATE = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1],
  [1,3,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,3,1],
  [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
  [1,2,1,1,2,1,2,1,1,1,2,1,1,0,0,1,1,2,1,1,1,2,1,2,1,1,2,1],
  [1,2,2,2,2,1,2,0,0,1,2,1,0,0,0,0,1,2,1,0,0,2,1,2,2,2,2,1],
  [1,1,1,1,2,1,0,0,1,1,2,0,0,1,1,0,0,2,1,1,0,0,1,0,1,1,1,1],
  [0,0,0,0,2,0,0,1,1,1,2,0,1,1,1,1,0,2,1,1,1,0,0,0,2,0,0,0],
  [1,1,1,1,2,1,0,0,1,1,2,0,0,1,1,0,0,2,1,1,0,0,1,0,1,1,1,1],
  [1,2,2,2,2,1,2,2,2,1,2,1,0,0,0,0,1,2,1,2,2,2,1,2,2,2,2,1],
  [1,2,1,1,2,1,2,1,1,1,2,1,1,0,0,1,1,2,1,1,1,2,1,2,1,1,2,1],
  [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
  [1,3,1,1,2,1,1,1,2,1,2,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,3,1],
  [1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
];

let maze, score, highScore = 0, lives, totalPellets;
let pacman, ghosts, fruits;
let paused = false;
let gameState = 'playing'; // playing, dying, respawning, won
let dyingTimer = 0, respawnTimer = 0;
let frame = 0;
let powerTimer = 0;

function initMaze() {
  maze = MAZE_TEMPLATE.map(row => [...row]);
  totalPellets = 0;
  for (let r=0;r<ROWS;r++) for(let c=0;c<COLS;c++) {
    if (maze[r][c]===2||maze[r][c]===3) totalPellets++;
  }
}

function initGame() {
  initMaze();
  score = 0;
  lives = 3;
  scoreEl.textContent = score;
  livesEl.textContent = '♥ '.repeat(lives).trim();
  msgEl.textContent = '';
  powerTimer = 0;
  gameState = 'playing';
  spawnPacman();
  spawnGhosts();
  fruits = [];
}

function spawnPacman() {
  pacman = {
    x: 14 * CELL + CELL/2,
    y: 11 * CELL + CELL/2,
    dir: { dx: 1, dy: 0 },
    nextDir: { dx: 1, dy: 0 },
    speed: 1.8,
    mouthAngle: 0.25,
    mouthOpen: true,
    mouthSpeed: 0.07,
    r: CELL*0.44,
  };
}

const GHOST_COLORS = ['#ff4466','#ffb8ff','#00ffff','#ffb852'];
const GHOST_NAMES  = ['Blinky','Pinky','Inky','Clyde'];

function spawnGhosts() {
  ghosts = [
    makeGhost(13, 6, GHOST_COLORS[0], 2.0, 0),
    makeGhost(14, 6, GHOST_COLORS[1], 1.8, 40),
    makeGhost(13, 7, GHOST_COLORS[2], 1.7, 80),
    makeGhost(14, 7, GHOST_COLORS[3], 1.6, 120),
  ];
}

function makeGhost(col, row, color, speed, delay) {
  return {
    x: col * CELL + CELL/2,
    y: row * CELL + CELL/2,
    dir: { dx: [-1,1,0,0][Math.floor(Math.random()*4)], dy: [0,0,-1,1][Math.floor(Math.random()*4)] },
    color, speed,
    frightened: false,
    eaten: false,
    r: CELL*0.46,
    delay,
    scatter: 0,
    scatterDir: {dx:0,dy:0},
  };
}

function cellAt(x, y) {
  const col = Math.floor(x / CELL);
  const row = Math.floor(y / CELL);
  if (col < 0 || col >= COLS || row < 0 || row >= ROWS) return 0;
  return maze[row][col];
}

function isWall(x, y) {
  return cellAt(x, y) === 1;
}

function canMove(entity, dx, dy) {
  const margin = entity.r * 0.8;
  const nx = entity.x + dx * entity.speed;
  const ny = entity.y + dy * entity.speed;
  const checks = [
    [nx - margin, ny - margin],
    [nx + margin, ny - margin],
    [nx - margin, ny + margin],
    [nx + margin, ny + margin],
  ];
  return checks.every(([cx, cy]) => !isWall(cx, cy));
}

function movePacman() {
  if (gameState !== 'playing') return;
  // Try next direction
  if (canMove(pacman, pacman.nextDir.dx, pacman.nextDir.dy)) {
    pacman.dir = { ...pacman.nextDir };
  }
  if (canMove(pacman, pacman.dir.dx, pacman.dir.dy)) {
    pacman.x += pacman.dir.dx * pacman.speed;
    pacman.y += pacman.dir.dy * pacman.speed;
  }
  // Wrap
  if (pacman.x < 0) pacman.x = W;
  if (pacman.x > W) pacman.x = 0;

  // Eat pellet
  const col = Math.floor(pacman.x / CELL);
  const row = Math.floor(pacman.y / CELL);
  if (row>=0&&row<ROWS&&col>=0&&col<COLS) {
    const cell = maze[row][col];
    if (cell === 2) {
      maze[row][col] = 4;
      score += 10;
      scoreEl.textContent = score;
      totalPellets--;
      if (totalPellets <= 0) { gameState = 'won'; msgEl.textContent = 'YOU WIN! Restarting...'; setTimeout(initGame, 2000); }
    } else if (cell === 3) {
      maze[row][col] = 4;
      score += 50;
      scoreEl.textContent = score;
      totalPellets--;
      powerTimer = 300;
      ghosts.forEach(g => { g.frightened = true; g.eaten = false; });
    }
  }

  // Mouth animation
  if (pacman.mouthOpen) {
    pacman.mouthAngle += pacman.mouthSpeed;
    if (pacman.mouthAngle >= 0.35) pacman.mouthOpen = false;
  } else {
    pacman.mouthAngle -= pacman.mouthSpeed;
    if (pacman.mouthAngle <= 0.02) pacman.mouthOpen = true;
  }
}

function moveGhosts() {
  if (gameState !== 'playing') return;
  if (powerTimer > 0) powerTimer--;
  if (powerTimer === 0) ghosts.forEach(g => { g.frightened = false; });

  ghosts.forEach((g, i) => {
    if (g.delay > 0) { g.delay--; return; }
    if (g.eaten) return;

    const scared = g.frightened;
    // Try to follow pac or scatter
    const dirs = [
      {dx:1,dy:0},{dx:-1,dy:0},{dx:0,dy:1},{dx:0,dy:-1}
    ].filter(d => canMove(g, d.dx, d.dy) && !(d.dx === -g.dir.dx && d.dy === -g.dir.dy));

    let chosen;
    if (dirs.length === 0) {
      chosen = { dx: -g.dir.dx, dy: -g.dir.dy };
    } else if (dirs.length === 1) {
      chosen = dirs[0];
    } else if (scared) {
      chosen = dirs[Math.floor(Math.random() * dirs.length)];
    } else {
      // Chase pac
      let target = { x: pacman.x, y: pacman.y };
      let best = Infinity, bestDir = dirs[0];
      dirs.forEach(d => {
        const nx = g.x + d.dx * CELL;
        const ny = g.y + d.dy * CELL;
        const dist = Math.hypot(nx - target.x, ny - target.y);
        if (dist < best) { best = dist; bestDir = d; }
      });
      // 20% random for fun
      chosen = Math.random() < 0.2 ? dirs[Math.floor(Math.random()*dirs.length)] : bestDir;
    }
    g.dir = chosen;
    g.x += chosen.dx * g.speed;
    g.y += chosen.dy * g.speed;
    if (g.x < 0) g.x = W; if (g.x > W) g.x = 0;
  });

  // Collision
  ghosts.forEach(g => {
    if (g.eaten) return;
    const dist = Math.hypot(pacman.x - g.x, pacman.y - g.y);
    if (dist < CELL * 0.75) {
      if (g.frightened) {
        g.eaten = true;
        g.frightened = false;
        score += 200;
        scoreEl.textContent = score;
        setTimeout(() => { g.eaten = false; g.x = 13*CELL+CELL/2; g.y = 6*CELL+CELL/2; }, 3000);
      } else if (gameState === 'playing') {
        gameState = 'dying';
        dyingTimer = 90;
        msgEl.textContent = '💥 Got caught!';
      }
    }
  });
}

// Spawn occasional fruit
function spawnFruit() {
  if (Math.random() < 0.003 && fruits.length < 2) {
    const fruitTypes = ['🍒','🍓','🍊','🍋','🍇','⭐'];
    fruits.push({
      x: (5 + Math.floor(Math.random()*18)) * CELL + CELL/2,
      y: (11 + Math.floor(Math.random()*2)) * CELL + CELL/2,
      type: fruitTypes[Math.floor(Math.random()*fruitTypes.length)],
      life: 300,
      points: [100,200,300,500,700,1000][Math.floor(Math.random()*6)],
    });
  }
  fruits = fruits.filter(f => {
    f.life--;
    const dist = Math.hypot(pacman.x - f.x, pacman.y - f.y);
    if (dist < CELL * 0.8) {
      score += f.points;
      scoreEl.textContent = score;
      if (score > highScore) { highScore = score; highEl.textContent = highScore; }
      return false;
    }
    return f.life > 0;
  });
}

// AI auto-pilot direction changes
let autoPilotTimer = 0;
function autoPilot() {
  autoPilotTimer--;
  if (autoPilotTimer > 0) return;
  autoPilotTimer = 8 + Math.floor(Math.random() * 20);
  const dirs = [
    {dx:1,dy:0},{dx:-1,dy:0},{dx:0,dy:1},{dx:0,dy:-1}
  ];
  // prefer direction toward nearest pellet
  let best = null, bestScore = -Infinity;
  dirs.forEach(d => {
    if (!canMove(pacman, d.dx, d.dy)) return;
    // look ahead a few cells
    let nx = pacman.x, ny = pacman.y, sc = 0;
    for (let s=0;s<5;s++) {
      nx += d.dx * CELL; ny += d.dy * CELL;
      const col = Math.floor(nx/CELL), row = Math.floor(ny/CELL);
      if (col<0||col>=COLS||row<0||row>=ROWS) break;
      const c = maze[row][col];
      if (c===1) { sc -= 20; break; }
      if (c===2) sc += 10;
      if (c===3) sc += 40;
      // avoid nearby frightened ghosts (avoid them when not powered)
      if (powerTimer === 0) {
        ghosts.forEach(g => {
          const gd = Math.hypot(nx - g.x, ny - g.y);
          if (gd < CELL*2) sc -= 30;
        });
      }
    }
    if (sc > bestScore) { bestScore = sc; best = d; }
  });
  if (best) pacman.nextDir = best;
  else {
    const valid = dirs.filter(d => canMove(pacman, d.dx, d.dy));
    if (valid.length) pacman.nextDir = valid[Math.floor(Math.random()*valid.length)];
  }
}

// ─── DRAW ───────────────────────────────────────────────────────────────────

function drawMaze() {
  for (let r=0;r<ROWS;r++) {
    for (let c=0;c<COLS;c++) {
      const cell = maze[r][c];
      const x = c*CELL, y = r*CELL;
      if (cell === 1) {
        // Wall gradient
        const grad = ctx.createLinearGradient(x,y,x+CELL,y+CELL);
        grad.addColorStop(0,'#1a1a6e');
        grad.addColorStop(1,'#0d0d55');
        ctx.fillStyle = grad;
        ctx.fillRect(x,y,CELL,CELL);
        // Neon border effect
        ctx.strokeStyle = '#4444ff';
        ctx.lineWidth = 1;
        ctx.strokeRect(x+0.5,y+0.5,CELL-1,CELL-1);
      } else {
        ctx.fillStyle = '#000010';
        ctx.fillRect(x,y,CELL,CELL);
        if (cell === 2) {
          // Pellet
          ctx.beginPath();
          ctx.arc(x+CELL/2, y+CELL/2, 3, 0, Math.PI*2);
          ctx.fillStyle = '#fffde0';
          ctx.fill();
          ctx.shadowColor = '#ffe600';
          ctx.shadowBlur = 6;
          ctx.fill();
          ctx.shadowBlur = 0;
        } else if (cell === 3) {
          // Power pellet pulse
          const pulse = 0.75 + 0.25 * Math.sin(frame * 0.12);
          ctx.beginPath();
          ctx.arc(x+CELL/2, y+CELL/2, 7*pulse, 0, Math.PI*2);
          ctx.fillStyle = '#ffe600';
          ctx.shadowColor = '#ffe600';
          ctx.shadowBlur = 18*pulse;
          ctx.fill();
          ctx.shadowBlur = 0;
        }
      }
    }
  }
}

function drawPacman() {
  if (gameState === 'dying') {
    // Death spin
    const spin = 1 - dyingTimer/90;
    const gap = spin * Math.PI;
    ctx.save();
    ctx.translate(pacman.x, pacman.y);
    ctx.rotate(gap);
    ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.arc(0,0,pacman.r, gap, Math.PI*2 - gap);
    ctx.closePath();
    const grad = ctx.createRadialGradient(0,0,0,0,0,pacman.r);
    grad.addColorStop(0,'#ffe600');
    grad.addColorStop(1,'#ff8800');
    ctx.fillStyle = grad;
    ctx.shadowColor = '#ffe600';
    ctx.shadowBlur = 16;
    ctx.fill();
    ctx.shadowBlur = 0;
    ctx.restore();
    return;
  }
  const angle = pacman.mouthAngle * Math.PI;
  const dir = Math.atan2(pacman.dir.dy, pacman.dir.dx);
  ctx.save();
  ctx.translate(pacman.x, pacman.y);
  ctx.rotate(dir);
  ctx.beginPath();
  ctx.moveTo(0,0);
  ctx.arc(0,0,pacman.r, angle, Math.PI*2-angle);
  ctx.closePath();
  const grad = ctx.createRadialGradient(-2,-2,0,0,0,pacman.r);
  grad.addColorStop(0,'#ffff44');
  grad.addColorStop(0.7,'#ffe600');
  grad.addColorStop(1,'#ffaa00');
  ctx.fillStyle = grad;
  ctx.shadowColor = '#ffe600';
  ctx.shadowBlur = 18;
  ctx.fill();
  ctx.shadowBlur = 0;
  // Eye
  ctx.beginPath();
  ctx.arc(pacman.r*0.25, -pacman.r*0.45, pacman.r*0.12, 0, Math.PI*2);
  ctx.fillStyle = '#000';
  ctx.fill();
  ctx.restore();
}

function drawGhost(g) {
  if (g.eaten) {
    // Ghost eyes floating back
    ctx.save();
    ctx.translate(g.x, g.y);
    drawGhostEyes(g.frightened);
    ctx.restore();
    return;
  }
  const frightFlash = g.frightened && powerTimer < 80 && Math.floor(frame/8)%2===0;
  const color = g.frightened ? (frightFlash ? '#ffffff' : '#2222ff') : g.color;
  ctx.save();
  ctx.translate(g.x, g.y);

  // Body
  const r = g.r;
  ctx.beginPath();
  ctx.arc(0, -r*0.1, r, Math.PI, 0);
  ctx.lineTo(r, r*0.8);
  // Wavy bottom
  const segments = 3;
  const segW = (r*2) / segments;
  for (let i = segments-1; i >= 0; i--) {
    const x1 = -r + segW*i + segW/2;
    const x2 = -r + segW*i;
    const wavY = (i%2===0) ? r*0.8 : r*0.4;
    ctx.quadraticCurveTo(x1, wavY, x2, r*0.8);
  }
  ctx.closePath();

  const grad = ctx.createLinearGradient(-r,-r,r,r);
  grad.addColorStop(0, color);
  grad.addColorStop(1, shadeColor(color, -40));
  ctx.fillStyle = grad;
  ctx.shadowColor = color;
  ctx.shadowBlur = 14;
  ctx.fill();
  ctx.shadowBlur = 0;

  if (!g.frightened) drawGhostEyes(false);
  else {
    // Scared face
    ctx.fillStyle = frightFlash ? '#0000ff' : '#ffffff';
    ctx.fillRect(-r*0.5,-r*0.2, r*0.3, r*0.25);
    ctx.fillRect(r*0.2,-r*0.2, r*0.3, r*0.25);
    ctx.fillStyle = frightFlash ? '#ffffff' : '#0000ff';
    ctx.beginPath();
    ctx.moveTo(-r*0.5, r*0.25);
    for (let xi=0;xi<6;xi++) {
      ctx.lineTo(-r*0.5 + xi*r/3, xi%2===0 ? r*0.1 : r*0.4);
    }
    ctx.lineWidth = 2;
    ctx.strokeStyle = ctx.fillStyle;
    ctx.stroke();
  }
  ctx.restore();
}

function drawGhostEyes(scared) {
  const r = CELL*0.46;
  if (!scared) {
    ctx.fillStyle = '#fff';
    ctx.beginPath(); ctx.ellipse(-r*0.35,-r*0.3,r*0.25,r*0.32,0,0,Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.ellipse(r*0.35,-r*0.3,r*0.25,r*0.32,0,0,Math.PI*2); ctx.fill();
    ctx.fillStyle = '#2244ff';
    ctx.beginPath(); ctx.arc(-r*0.32,-r*0.22,r*0.14,0,Math.PI*2); ctx.fill();
    ctx.beginPath(); ctx.arc(r*0.38,-r*0.22,r*0.14,0,Math.PI*2); ctx.fill();
  }
}

function shadeColor(color, amount) {
  let col = color.replace('#','');
  if (col.length === 3) col = col.split('').map(c=>c+c).join('');
  let r = parseInt(col.substring(0,2),16);
  let g = parseInt(col.substring(2,4),16);
  let b = parseInt(col.substring(4,6),16);
  r = Math.max(0,Math.min(255,r+amount));
  g = Math.max(0,Math.min(255,g+amount));
  b = Math.max(0,Math.min(255,b+amount));
  return '#'+[r,g,b].map(x=>x.toString(16).padStart(2,'0')).join('');
}

function drawFruits() {
  fruits.forEach(f => {
    ctx.font = `${CELL*0.85}px serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    const bob = Math.sin(frame * 0.1) * 3;
    ctx.fillText(f.type, f.x, f.y + bob);
  });
}

function drawParticles() {} // placeholder for future sparkles

// ─── LOOP ───────────────────────────────────────────────────────────────────

function update() {
  frame++;
  if (gameState === 'dying') {
    dyingTimer--;
    if (dyingTimer <= 0) {
      lives--;
      livesEl.textContent = '♥ '.repeat(Math.max(0,lives)).trim() || '💀';
      if (lives <= 0) {
        gameState = 'won'; // restart
        if (score > highScore) highScore = score;
        highEl.textContent = highScore;
        msgEl.textContent = '💀 GAME OVER — Restarting...';
        setTimeout(initGame, 2500);
      } else {
        spawnPacman();
        gameState = 'playing';
        msgEl.textContent = '';
      }
    }
    return;
  }
  autoPilot();
  movePacman();
  moveGhosts();
  spawnFruit();
}

function draw() {
  ctx.clearRect(0, 0, W, H);
  drawMaze();
  drawFruits();
  drawPacman();
  ghosts.forEach(drawGhost);
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}

initGame();
loop();
</script>
</body>
</html>
"""
    components.html(pacman_html, height=440, scrolling=False)
    section_end()


def render_cv() -> None:

    section_start("cv")
    section_title("My CV", "📜")
    st.caption("A glance at my professional background and skills available for direct access.")

    cv_link = "https://canva.link/cmn3h8sq33jeuib"
    preview_url = "https://www.canva.com/design/DAGzcHTtmzQ/uGneX3fzgU2Q1zRfhlCTRA/view?embed"

    col1, col2 = st.columns([1.1, 1], gap="large")
    with col1:
        st.markdown(
            f"""
            <div class="experience-card cv-access-card">
                <div class="experience-card-inner" style="justify-content: center; padding: 2.2rem;">
                    <h3 style="margin-top: 0; margin-bottom: 0.5rem; color: var(--accent-2);">📄 Instant Access to Resume</h3>
                    <p style="margin-bottom: 1.5rem; color: var(--muted); line-height: 1.6; font-size: 0.98rem;">
                        View my updated CV on Canva. Inside, you'll find a detailed listing of my academic computer engineering background, complete technical experiences and project snapshots.
                    </p>
                    <div style="display: flex; flex-direction: column; gap: 0.82rem; width: 100%; margin-top: auto;">
                        <a class="st-link-button" href="{cv_link}" target="_blank" style="text-decoration: none !important;">🎨 View CV on Canva</a>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div class="experience-card cv-preview-card">
                <div class="experience-card-inner" style="padding: 0; overflow: hidden; justify-content: center;">
                    <iframe src="{preview_url}" width="100%" height="380" style="border: none; display: block;" allowfullscreen="allowfullscreen" allow="fullscreen"></iframe>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    section_end()


def render_contact() -> None:
    section_start("contact")
    section_title("Contact", "📬")
    st.caption("Send a direct message — it opens your email client with everything pre‑filled.")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        sender_email = st.text_input("Your Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message", height=160)
        submitted = st.form_submit_button("📨 Send Message")

    if submitted:
        body = f"Name: {name}\nEmail: {sender_email}\n\n{message}"
        mailto = (
            f"mailto:{PROFILE['email']}?subject={quote(subject)}"
            f"&body={quote(body)}"
        )
        st.markdown(f"[Click here to send your email]({mailto})")

    st.markdown("---")
    st.caption(f"© {datetime.now().year} {PROFILE['name']} · Built with Streamlit")
    section_end()


def mount_scroll_behavior() -> None:
    st.markdown("<div class='scroll-progress' id='scroll-progress'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <script>
            (() => {
                const SIDE_LINK_SELECTOR = '.nav-link';
                const SECTION_SELECTOR = '.anchor-section';
                const duration = 600;

                const easeInOut = (t) => {
                    return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
                };

                const smoothScrollTo = (targetY) => {
                    const startY = window.pageYOffset;
                    const distance = targetY - startY;
                    let startTime = null;

                    const tick = (currentTime) => {
                        if (!startTime) startTime = currentTime;
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const eased = easeInOut(progress);
                        window.scrollTo(0, startY + distance * eased);
                        if (elapsed < duration) {
                            window.requestAnimationFrame(tick);
                        }
                    };

                    window.requestAnimationFrame(tick);
                };

                const updateProgress = () => {
                    const el = document.getElementById('scroll-progress');
                    if (!el) return;
                    const scrollTop = window.pageYOffset;
                    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
                    const ratio = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
                    el.style.width = `${Math.min(100, Math.max(0, ratio))}%`;
                };

                const links = Array.from(document.querySelectorAll(SIDE_LINK_SELECTOR));
                links.forEach((link) => {
                    link.addEventListener('click', (event) => {
                        event.preventDefault();
                        const targetId = link.dataset.target;
                        const target = document.getElementById(targetId);
                        if (!target) return;
                        const top = target.getBoundingClientRect().top + window.pageYOffset - 10;
                        smoothScrollTo(top);
                    });
                });

                const observeSkillCards = () => {
                    const revealCards = Array.from(
                        document.querySelectorAll('.skill-fade-in, .lang-fade-in')
                    );
                    if (!revealCards.length) return;

                    const skillObserver = new IntersectionObserver(
                        (entries) => {
                            entries.forEach((entry) => {
                                if (entry.isIntersecting) {
                                    entry.target.classList.add('is-visible');
                                    skillObserver.unobserve(entry.target);
                                }
                            });
                        },
                        {
                            root: null,
                            rootMargin: '0px 0px -12% 0px',
                            threshold: 0.08,
                        }
                    );

                    revealCards.forEach((card, index) => {
                        card.style.transitionDelay = `${Math.min(index * 35, 180)}ms`;
                        skillObserver.observe(card);
                    });
                };

                const setActive = (anchor) => {
                    links.forEach((link) => {
                        const isActive = link.dataset.target === anchor;
                        link.classList.toggle('active', isActive);
                    });
                };

                const sections = Array.from(document.querySelectorAll(SECTION_SELECTOR));
                if (sections.length) {
                    const observer = new IntersectionObserver(
                        (entries) => {
                            entries.forEach((entry) => {
                                if (entry.isIntersecting) {
                                    const anchor = entry.target.dataset.anchor;
                                    if (anchor) setActive(anchor);
                                }
                            });
                        },
                        {
                            root: null,
                            rootMargin: '-40% 0px -45% 0px',
                            threshold: 0.01,
                        }
                    );
                    sections.forEach((section) => observer.observe(section));
                }

                setActive('hero');
                updateProgress();
                observeSkillCards();
                setTimeout(observeSkillCards, 350);
                window.addEventListener('scroll', updateProgress, { passive: true });
            })();
        </script>
        """,
        unsafe_allow_html=True,
    )
