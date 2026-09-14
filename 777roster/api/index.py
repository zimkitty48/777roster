from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>777 ROSTER</title>

<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;800;900&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background: #02050a;
    color: white;
    min-height: 100vh;
    overflow-x: hidden;
    font-family: "Courier New", monospace;
}

body.locked {
    overflow: hidden;
}


/* =========================================
   BACKGROUND
========================================= */

#network {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    z-index: -10;
    overflow: hidden;

    background:
        radial-gradient(
            circle at center,
            rgba(0, 90, 255, .12),
            transparent 55%
        ),
        #02050a;
}

.network-dot {
    position: absolute;

    width: 4px;
    height: 4px;

    border-radius: 50%;

    background: #168cff;

    box-shadow:
        0 0 5px #168cff,
        0 0 12px rgba(0, 120, 255, .8),
        0 0 25px rgba(0, 100, 255, .4);

    animation: dotPulse 2s infinite alternate;
}

.network-line {
    position: absolute;

    height: 1px;

    background: rgba(0, 130, 255, .25);

    transform-origin: left center;

    box-shadow:
        0 0 5px rgba(0, 130, 255, .4);
}

@keyframes dotPulse {

    from {
        opacity: .35;
        transform: scale(.7);
    }

    to {
        opacity: 1;
        transform: scale(1.5);
    }

}

.blue-particle {
    position: fixed;

    width: 2px;
    height: 2px;

    background: #168cff;

    border-radius: 50%;

    box-shadow:
        0 0 8px #168cff;

    animation:
        particleFloat linear infinite;
}

@keyframes particleFloat {

    from {
        transform: translateY(110vh);
        opacity: 0;
    }

    10% {
        opacity: .8;
    }

    90% {
        opacity: .8;
    }

    to {
        transform: translateY(-10vh);
        opacity: 0;
    }

}


/* =========================================
   CLICK TO ENTER
========================================= */

#landing {
    position: fixed;

    inset: 0;

    z-index: 100;

    display: flex;

    align-items: center;

    justify-content: center;

    flex-direction: column;

    background:
        radial-gradient(
            circle at center,
            rgba(0, 100, 255, .18),
            transparent 50%
        ),
        linear-gradient(
            rgba(0, 5, 20, .55),
            rgba(0, 0, 10, .92)
        ),
        #02050a;

    transition:
        opacity .8s ease,
        visibility .8s ease;
}

#landing.hide {
    opacity: 0;

    visibility: hidden;

    pointer-events: none;
}

.landing-grid {
    position: absolute;

    inset: 0;

    opacity: .25;

    background-image:
        linear-gradient(
            rgba(0, 120, 255, .12) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(0, 120, 255, .12) 1px,
            transparent 1px
        );

    background-size: 60px 60px;
}

.landing-content {
    position: relative;

    z-index: 2;

    text-align: center;

    padding: 30px;
}

.small-title {
    color: #168cff;

    font-size: 13px;

    letter-spacing: 8px;

    margin-bottom: 18px;

    text-shadow:
        0 0 10px #168cff;
}

.landing-logo {
    font-family: Orbitron, sans-serif;

    font-size:
        clamp(75px, 14vw, 180px);

    font-weight: 900;

    letter-spacing: 15px;

    color: #168cff;

    text-shadow:
        0 0 5px #168cff,
        0 0 15px #168cff,
        0 0 35px #0077ff,
        0 0 70px #0055ff,
        0 0 120px rgba(0, 100, 255, .5);

    animation:
        landingPulse 2.5s infinite alternate;
}

@keyframes landingPulse {

    from {
        filter: brightness(.8);
    }

    to {
        filter: brightness(1.5);
    }

}

.landing-subtitle {
    margin-top: 5px;

    color: #d7eaff;

    font-family: Orbitron, sans-serif;

    font-size: 18px;

    font-weight: bold;

    letter-spacing: 9px;

    text-shadow:
        0 0 10px #168cff;
}

.enter {
    margin-top: 55px;

    padding: 18px 42px;

    border: 1px solid #168cff;

    background:
        rgba(0, 100, 255, .08);

    color: #168cff;

    font-family: Orbitron, sans-serif;

    font-size: 14px;

    font-weight: 800;

    letter-spacing: 4px;

    cursor: pointer;

    box-shadow:
        0 0 10px rgba(0, 110, 255, .5),
        inset 0 0 10px rgba(0, 110, 255, .15);

    transition: .3s;
}

.enter:hover {

    transform: scale(1.08);

    color: white;

    background:
        rgba(0, 100, 255, .22);

    box-shadow:
        0 0 15px #168cff,
        0 0 35px #006cff,
        0 0 65px rgba(0, 100, 255, .55);
}

.enter:active {
    transform: scale(.98);
}


/* =========================================
   MAIN
========================================= */

#main {
    min-height: 100vh;

    opacity: 0;

    transform:
        translateY(30px);

    transition:
        1s ease;
}

#main.show {
    opacity: 1;

    transform:
        translateY(0);
}


/* =========================================
   HEADER
========================================= */

.header {
    text-align: center;

    padding:
        38px 20px 15px;
}

.logo {
    font-family:
        Orbitron, sans-serif;

    font-size:
        clamp(45px, 6vw, 78px);

    font-weight: 900;

    letter-spacing: 8px;

    color: #168cff;

    text-shadow:
        0 0 5px #168cff,
        0 0 15px #168cff,
        0 0 30px rgba(0, 120, 255, .9),
        0 0 60px rgba(0, 80, 255, .5);

    animation:
        titlePulse 2.5s infinite alternate;
}

@keyframes titlePulse {

    from {
        text-shadow:
            0 0 5px #168cff,
            0 0 15px #168cff;
    }

    to {
        text-shadow:
            0 0 8px #168cff,
            0 0 20px #168cff,
            0 0 45px #168cff,
            0 0 75px rgba(0, 100, 255, .7);
    }

}

.subtitle {
    margin-top: 25px;

    color: #168cff;

    font-size: 13px;

    font-weight: bold;

    letter-spacing: 5px;

    text-shadow:
        0 0 8px #168cff;
}


/* =========================================
   ROSTER
========================================= */

.roster-wrapper {

    width:
        min(900px, 92%);

    margin:
        35px auto 80px;
}


/* =========================================
   CATEGORY
========================================= */

.category {

    position: relative;

    margin: 30px 0;

    padding:
        15px 20px 18px;

    background:
        rgba(0, 2, 8, .82);

    border:
        1px solid
        rgba(0, 130, 255, .35);

    border-radius:
        22px;

    backdrop-filter:
        blur(12px);

    box-shadow:
        0 0 25px rgba(0,0,0,.7),
        inset 0 0 35px
        rgba(0,100,255,.02);
}

.category-title {

    display: flex;

    align-items: center;

    height: 35px;

    margin-bottom: 15px;

    padding-left: 13px;

    border-left:
        5px solid
        var(--category);

    color:
        var(--category);

    font-family:
        Orbitron, sans-serif;

    font-size: 22px;

    font-weight: 900;

    letter-spacing: 3px;

    text-shadow:
        0 0 7px var(--category),
        0 0 15px var(--category);
}


/* =========================================
   MEMBER
========================================= */

.member {

    position: relative;

    display: flex;

    align-items: center;

    min-height: 92px;

    margin: 12px 0;

    padding:
        12px 18px;

    background:
        #080b10;

    border:
        1px solid
        rgba(255,255,255,.12);

    border-left:
        5px solid
        var(--category);

    border-radius:
        40px;

    transition:
        transform .25s ease,
        border-color .25s ease,
        box-shadow .25s ease;
}

.member:hover {

    transform:
        translateX(7px);

    border-color:
        var(--category);

    box-shadow:
        0 0 25px
        rgba(0, 120, 255, .18),

        inset 0 0 20px
        rgba(0,100,255,.025);
}


/* =========================================
   AVATAR
========================================= */

.avatar {

    width: 66px;

    height: 66px;

    min-width: 66px;

    border-radius: 50%;

    object-fit: cover;

    border:
        2px solid #dfeaff;

    margin-right: 20px;

    background:
        #05080c;

    box-shadow:
        0 0 7px
        rgba(255,255,255,.25);

    transition:
        .3s;
}

.member:hover .avatar {

    border-color:
        var(--category);

    box-shadow:
        0 0 8px var(--category),
        0 0 20px var(--category);

    transform:
        scale(1.05);
}


/* =========================================
   MEMBER TEXT
========================================= */

.member-info {
    min-width: 0;
}

.member-name {

    color:
        var(--category);

    font-family:
        Orbitron, sans-serif;

    font-size: 19px;

    font-weight: 900;

    letter-spacing: 1px;

    text-shadow:
        0 0 8px var(--category);
}

.member-description {

    margin-top: 6px;

    color:
        #a8aeb8;

    font-size: 12px;

    line-height: 1.4;
}

.question {

    font-size: 25px;

    letter-spacing: 5px;
}


/* =========================================
   CATEGORY COLORS
========================================= */

.owner {
    --category: #ff55df;
}

.coowner {
    --category: #ffd83d;
}

.admin {
    --category: #00bfff;
}

.skid {
    --category: #70ffb0;
}

.larp {
    --category: #168cff;
}

.femboy {
    --category: #82adff;
}


/* =========================================
   QUESTION AVATARS
========================================= */

.question-avatar {

    display: flex;

    align-items: center;

    justify-content: center;

    color:
        var(--category);

    font-size: 25px;

    font-weight: bold;

    text-shadow:
        0 0 10px var(--category);
}


/* =========================================
   FOOTER
========================================= */

.footer {

    text-align: center;

    padding:
        40px 20px 60px;

    color:
        #3f4a59;

    font-size: 11px;

    letter-spacing: 4px;
}

.footer span {

    color:
        #168cff;

    text-shadow:
        0 0 8px #168cff;
}


/* =========================================
   SCROLLBAR
========================================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background:
        #02050a;
}

::-webkit-scrollbar-thumb {

    background:
        #073d78;

    border-radius:
        10px;
}

::-webkit-scrollbar-thumb:hover {

    background:
        #168cff;

    box-shadow:
        0 0 10px #168cff;
}


/* =========================================
   MOBILE
========================================= */

@media(max-width: 650px) {

    .header {
        padding-top: 25px;
    }

    .logo {
        letter-spacing: 4px;
    }

    .subtitle {
        font-size: 8px;
        letter-spacing: 2px;
    }

    .roster-wrapper {
        width: 95%;
    }

    .category {
        padding:
            13px 10px;

        border-radius:
            18px;
    }

    .category-title {
        font-size: 17px;
    }

    .member {
        padding:
            10px 12px;

        min-height:
            82px;
    }

    .avatar {
        width: 54px;
        height: 54px;
        min-width: 54px;

        margin-right: 13px;
    }

    .member-name {
        font-size: 15px;
    }

    .member-description {
        font-size: 10px;
    }

    .landing-logo {
        letter-spacing: 6px;
    }

    .landing-subtitle {
        font-size: 13px;
        letter-spacing: 5px;
    }

}

</style>
</head>


<body class="locked">


<!-- =========================================
     BACKGROUND
========================================= -->

<div id="network"></div>


<!-- =========================================
     CLICK TO ENTER
========================================= -->

<div id="landing">

    <div class="landing-grid"></div>

    <div class="landing-content">

        <div class="small-title">
            777 DEVELOPMENT
        </div>

        <div class="landing-logo">
            777
        </div>

        <div class="landing-subtitle">
            ROSTER
        </div>

        <button
            class="enter"
            onclick="enterSite()"
        >
            CLICK TO SEE ROSTER
        </button>

    </div>

</div>


<!-- =========================================
     MAIN WEBSITE
========================================= -->

<div id="main">


<header class="header">

    <div class="logo">
        777 ROSTER
    </div>

    <div class="subtitle">
        NEWEST AND MOST ACTIVE MEMBERS OF 777 | DM @.1YHP TO BE ADDED
    </div>

</header>


<main class="roster-wrapper">


<!-- =========================================
     OWNER
========================================= -->

<section class="category owner">

    <div class="category-title">
        OWNER
    </div>


    <div class="member">

        <img
            class="avatar"
            src="https://cdn.discordapp.com/avatars/1209235945824583731/705ddc83bbda5e45f6d0cf897e527bdd.webp?size=1024"
            onerror="this.src='https://ui-avatars.com/api/?name=POWA&background=111&color=ff55df'"
        >

        <div class="member-info">

            <div class="member-name">
                POWA
            </div>

            <div class="member-description">
                Owner of 777.
            </div>

        </div>

    </div>


    <div class="member">

        <img
            class="avatar"
            src="https://cdn.discordapp.com/avatars/1423447234493550602/c6886414fc3ac18dd33c2eb46b3cab37.webp?size=1024"
            onerror="this.src='https://ui-avatars.com/api/?name=ASTEROID&background=111&color=ff55df'"
        >

        <div class="member-info">

            <div class="member-name">
                ASTEROID
            </div>

            <div class="member-description">
                Owner of 777.
            </div>

        </div>

    </div>


    <div class="member">

        <img
            class="avatar"
            src="https://cdn.discordapp.com/avatars/1339217256650899588/a_969af90021ba1b376fb289ccfe0f84fa.webp?size=1024&animated=true"
            onerror="this.src='https://ui-avatars.com/api/?name=DEATH&background=111&color=ff55df'"
        >

        <div class="member-info">

            <div class="member-name">
                DEATH
            </div>

            <div class="member-description">
                Owner of 777.
            </div>

        </div>

    </div>

</section>


<!-- =========================================
     CO OWNER
========================================= -->

<section class="category coowner">

    <div class="category-title">
        CO OWNER
    </div>


    <div class="member">

        <img
            class="avatar"
            src="https://cdn.discordapp.com/avatars/1529816081135308951/28d6dce625cd6e88221f029f32b62290.webp?size=1024"
            onerror="this.src='https://ui-avatars.com/api/?name=SADCAT&background=111&color=ffd83d'"
        >

        <div class="member-info">

            <div class="member-name">
                SADCAT
            </div>

            <div class="member-description">
                Co-owner of 777.
            </div>

        </div>

    </div>

</section>


<!-- =========================================
     ADMIN
========================================= -->

<section class="category admin">

    <div class="category-title">
        ADMIN
    </div>


    <div class="member">

        <div class="avatar question-avatar">
            ?
        </div>

        <div class="member-info">

            <div class="member-name question">
                ?
            </div>

            <div class="member-description">
                777 administration.
            </div>

        </div>

    </div>

</section>


<!-- =========================================
     SKID
========================================= -->

<section class="category skid">

    <div class="category-title">
        SKID
    </div>


    <div class="member">

        <div class="avatar question-avatar">
            ?
        </div>

        <div class="member-info">

            <div class="member-name question">
                ?
            </div>

            <div class="member-description">
                777 roster member.
            </div>

        </div>

    </div>

</section>


<!-- =========================================
     LARP
========================================= -->

<section class="category larp">

    <div class="category-title">
        LARP
    </div>


    <div class="member">

        <div class="avatar question-avatar">
            ?
        </div>

        <div class="member-info">

            <div class="member-name question">
                ?
            </div>

            <div class="member-description">
                777 roster member.
            </div>

        </div>

    </div>

</section>


<!-- =========================================
     FEMBOY
========================================= -->

<section class="category femboy">

    <div class="category-title">
        FEMBOY
    </div>


    <div class="member">

        <div class="avatar question-avatar">
            ?
        </div>

        <div class="member-info">

            <div class="member-name question">
                ?
            </div>

            <div class="member-description">
                777 roster member.
            </div>

        </div>

    </div>

</section>


</main>


<footer class="footer">

    777 ROSTER —
    <span>2026</span>

</footer>


</div>


<!-- =========================================
     HIDDEN MUSIC
========================================= -->

<audio
    id="backgroundMusic"
    loop
    preload="auto"
>
    <source
        src="https://cdn.discordapp.com/attachments/1535818104414928977/1538530286382612600/Shot_Callin.mp3?ex=6aa93efc&is=6aa7ed7c&hm=29110df1759d2aa3410505dc299943aef5149cb867afa3d45e438803c9265f37&"
        type="audio/mpeg"
    >
</audio>


<script>

/* =========================================
   CREATE BACKGROUND NODES
========================================= */

const network =
    document.getElementById("network");

const nodes = [];

const nodeCount = 85;


for (
    let i = 0;
    i < nodeCount;
    i++
) {

    const node =
        document.createElement("div");

    node.className =
        "network-dot";

    const x =
        Math.random() * 100;

    const y =
        Math.random() * 100;

    node.style.left =
        x + "%";

    node.style.top =
        y + "%";

    node.style.animationDelay =
        Math.random() * 2 + "s";

    network.appendChild(node);

    nodes.push({
        x: x,
        y: y
    });

}


/* =========================================
   CONNECT NODES
========================================= */

for (
    let i = 0;
    i < nodes.length;
    i++
) {

    for (
        let j = i + 1;
        j < nodes.length;
        j++
    ) {

        const a =
            nodes[i];

        const b =
            nodes[j];

        const dx =
            b.x - a.x;

        const dy =
            b.y - a.y;

        const distance =
            Math.sqrt(
                dx * dx +
                dy * dy
            );

        if (
            distance < 15
        ) {

            const line =
                document.createElement("div");

            line.className =
                "network-line";

            const width =
                Math.sqrt(

                    Math.pow(
                        dx *
                        window.innerWidth /
                        100,
                        2
                    )

                    +

                    Math.pow(
                        dy *
                        window.innerHeight /
                        100,
                        2
                    )

                );

            const angle =
                Math.atan2(
                    dy * window.innerHeight,
                    dx * window.innerWidth
                ) *
                180 /
                Math.PI;

            line.style.width =
                width + "px";

            line.style.left =
                a.x + "%";

            line.style.top =
                a.y + "%";

            line.style.transform =
                `rotate(${angle}deg)`;

            network.appendChild(line);
        }

    }

}


/* =========================================
   FLOATING PARTICLES
========================================= */

for (
    let i = 0;
    i < 35;
    i++
) {

    const particle =
        document.createElement("div");

    particle.className =
        "blue-particle";

    particle.style.left =
        Math.random() * 100 + "%";

    particle.style.animationDuration =
        (
            Math.random() * 12 + 8
        ) + "s";

    particle.style.animationDelay =
        Math.random() * 10 + "s";

    network.appendChild(particle);

}


/* =========================================
   ENTER WEBSITE + START MUSIC
========================================= */

function enterSite() {

    const landing =
        document.getElementById("landing");

    const main =
        document.getElementById("main");

    const music =
        document.getElementById("backgroundMusic");


    /* Hide landing */

    landing.classList.add("hide");


    /* Show roster */

    main.classList.add("show");


    /* Unlock scrolling */

    document.body.classList.remove("locked");


    /* Start music */

    music.volume = 1.0;

    music.play()
        .catch(function(error) {

            console.log(
                "Music could not start:",
                error
            );

        });

}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


