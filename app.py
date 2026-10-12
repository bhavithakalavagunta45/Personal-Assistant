from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def home():
    return """
    <body style="
        text-align:center;
        font-family:Arial;
        background-color:white !important; "
    >
    <h1> My personal assistant<br></h1>
    <a href="/entertainment">
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Entertainment</button>
    </a>
    <br>
    <a href=/study>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Study</button>
    </a><br>
    <a href=/cooking>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Cooking</button>
    </a><br>
    <a href=/motivation>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Motivation</button>
    </a><br>
    <a href=/fitness>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Fitness</button>
    </a><br>
    <a href=/funfacts>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Funfacts</button>
    </a><br>
    <a href=/budget>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Budget Planner</button>
    </a><br>
    <a href=/calculator>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Calculator</button>
    </a><br>
    """
@app.route("/entertainment")
def entertainment():
    return """
    <h1>Entertainment</h1>
    <a href=/movies>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Movies</button>
    </a><br>
    <a href=/webseries>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Web-series</button>
    </a><br>
    <a href=/animes>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Animes</button>
    </a><br>
    <a href=/riddles>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Riddles</button>
    </a><br>
    <a href=/jokes>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Jokes</button>
    </a><br>
    <a href=/cartoons>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Cartoons</button>
    </a><br>
    """
@app.route("/riddles")
def riddles():
    return """
    <h1>Riddles</h1>
    <br><br>⭐What has keys but can't open locks?
<br>-->Answer: A piano
<br><br>⭐What has hands but can't clap?
<br>-->Answer: A clock
<br><br>⭐What gets wetter as it dries?
<br>-->Answer: A towel
<br><br>⭐What has a neck but no head?
<br>-->Answer: A bottle
<br><br>⭐What can travel around the world while staying in one corner?
<br>-->Answer: A stamp
<br><br>⭐What has one eye but cannot see?
<br>-->Answer: A needle
<br><br>⭐What goes up but never comes down?
<br>-->Answer: Your age
<br><br>⭐What has many teeth but can't bite?
<br>-->Answer: A comb
<br><br>⭐What comes once in a minute, twice in a moment, but never in a thousand years?
<br>-->Answer: The letter M
<br><br>⭐What has a face and two hands but no arms or legs?
<br>-->Answer: A clock
<br><br>⭐What begins with T, ends with T, and has T in it?
<br>-->Answer: A teapot
<br><br>⭐What is full of holes but still holds water?
<br>-->Answer: A sponge
<br><br>⭐What can you catch but not throw?
<br>-->Answer: A cold
<br><br>⭐What has legs but doesn't walk?
<br>-->Answer: A table
<br><br>⭐What belongs to you but is used more by others?
<br>-->Answer: Your name
<br><br>⭐What has words but never speaks?
<br>-->Answer: A book
<br><br>⭐What can run but never walks?
<br>-->Answer: Water
<br><br>⭐What has a thumb and four fingers but isn't alive?
<br>-->Answer: A glove
<br><br>⭐What goes through cities and fields but never moves?
<br>-->Answer: A road
<br><br>⭐What comes down but never goes up?
<br>-->Answer: Rain
<br><br>⭐What has an endless supply of letters but starts empty?
<br>-->Answer: A mailbox
<br><br>⭐What can fill a room but takes no space?
<br>-->Answer: Light
<br><br>⭐What is always in front of you but can't be seen?
<br>-->Answer: The future
<br><br>⭐What has an eye but cannot see?
<br>-->Answer: A hurricane
<br><br>⭐What kind of room has no doors or windows?
<br>-->Answer: A mushroom
<br><br>⭐What can you break without touching it?
<br>-->Answer: A promise
<br><br>⭐What goes up and down but doesn't move?
<br>-->Answer: Stairs
<br><br>⭐What has a head, a tail, but no body?
<br>-->Answer: A coin
<br><br>⭐What can be cracked, made, told, and played?
<br>-->Answer: A joke
<br><br>⭐What gets bigger the more you take away?
<br>-->Answer: A hole
<br><br>⭐What has four wheels and flies?
<br>-->Answer: A garbage truck
<br><br>⭐What has cities but no houses?
<br>-->Answer: A map
<br><br>⭐What can you hear but not see or touch?
<br>-->Answer: Your voice
<br><br>⭐What is so fragile that saying its name breaks it?
<br>-->Answer: Silence
<br><br>⭐What invention lets you look right through a wall?
<br>-->Answer: A window
<br><br>⭐What has roots nobody sees?
<br>-->Answer: A tree
<br><br>⭐What is easy to lift but hard to throw?
<br>-->Answer: A feather
<br><br>⭐What goes around the world but stays in a corner?
<br>-->Answer: A stamp
<br><br>⭐What is black when clean and white when dirty?
<br>-->Answer: A blackboard
<br><br>⭐What can be measured but has no length, width, or height?
<br>-->Answer: Time
<br><br>⭐What has one head, one foot, and four legs?
<br>-->Answer: A bed
<br><br>⭐What kind of coat is always wet when you put it on?
<br>-->Answer: A coat of paint
<br><br>⭐What can you keep after giving it away?
<br>-->Answer: Your word
<br><br>⭐What goes up when rain comes down?
<br>-->Answer: An umbrella
<br><br>⭐What has a ring but no finger?
<br>-->Answer: A telephone
<br><br>⭐What can you hold in your left hand but not in your right hand?
<br>-->Answer: Your right elbow
<br><br>⭐What has no life but can die?
<br>-->Answer: A battery
<br><br>⭐What is lighter than a feather but no one can hold it for long?
<br>-->Answer: Breath
<br><br>⭐What starts with E, ends with E, and contains one letter?
<br>-->Answer: An envelope
<br><br>⭐What has an answer but never asks a question?
<br>-->Answer: A doorbell
    """
@app.route("/cartoons")
def cartoons():
    return """
    <h1>Cartoons</h1>
•Tom and Jerry<br>•
Doraemon<br>•
Shin Chan<br>•
Pokémon<br>•
Ben 10<br>•
Oggy and the Cockroaches<br>•
Mr. Bean: The Animated Series<br>•
The Powerpuff Girls<br>•
Scooby-Doo, Where Are You!<br>•
The Flintstones<br>•
The Jetsons<br>•
Looney Tunes<br>•
DuckTales<br>•
The Smurfs<br>•
Johnny Bravo<br>•
Dexter's Laboratory<br>•
Ed, Edd n Eddy<br>•
Courage the Cowardly Dog<br>•
Codename: Kids Next Door<br>•
The Grim Adventures of Billy & Mandy<br>•
Adventure Time<br>•
Regular Show<br>•
Steven Universe<br>•
We Bare Bears<br>•
The Amazing World of Gumball<br>•
Teen Titans Go!<br>•
Avatar: The Last Airbender<br>•
The Legend of Korra<br>•
SpongeBob SquarePants<br>•
The Fairly OddParents<br>•
Phineas and Ferb<br>•
Kim Possible<br>•
Gravity Falls<br>•
Star vs. the Forces of Evil<br>•
Bluey<br>•
Mickey Mouse Clubhouse<br>•
Paw Patrol<br>•
Peppa Pig<br>•
Chhota Bheem<br>•
Motu Patlu<br>•
Roll No 21<br>•
Little Singham<br>•
Bandbudh Aur Budbak<br>•
Rudra<br>•
KochiKame<br>•
Beyblade<br>•
Dragon Ball Z<br>•
Naruto<br>•
One Piece<br>
Attack on Titan<br>
    """
@app.route("/movies")
def movies():
    return """
    <h1>Movies</h1>
    <a href=/action>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Action</button>
    </a><br>
    <a href=/comedy>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Comedy</button>
    </a><br>
    <a href=/scifi>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Sci-fi</button>
    </a><br>
    <a href=/horror>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Horror</button>
    </a><br>
    <a href=/family>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Family</button>
    </a><br>
    """
@app.route("/webseries")
def webseries():
    return """
    <h1>Web series</h1>
    <a href=/comedy>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Comedy</button>
    </a><br>
    <a href=/kdrama>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >K-drama</button>
    </a><br>
    <a href=/fantasy>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Fantasy</button>
    </a><br>
    <a href=/thriller>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Thriller</button>
    </a><br>
    """
@app.route("/thriller")
def thriller():
    return """
    <h1>Thriller web series</h1>
<h3>Korean Thriller Series</h3><br>
The Glory<br>•
Flower of Evil<br>•
Mouse<br>•
Beyond Evil<br>•
Signal<br>•
Stranger<br>•
My Name<br>•
Vincenzo<br>•
Weak Hero Class 1<br>•
A Shop for Killers<br><br>
<h3>International Thriller Series</h3><br>
Breaking Bad<br>•
Better Call Saul<br>•
Dark<br>•
Mindhunter<br>•
Ozark<br>•
You<br>•
Money Heist<br>•
Prison Break<br>•
Sherlock<br>•
Severance<br><br>
<h3>Mystery & Mind-Bending Thrillers</h3><br>
Black Mirror<br>•
1899<br>•
The Sinner<br>•
True Detective<br>•
Bodyguard<br><br>
<h2>Top 5 Thriller Series with Major Twists</h2><br>
•Dark<br>
Mouse<br>•
Flower of Evil<br>•
Mindhunter<br>•
Beyond Evil<br>
    """
@app.route("/fantasy")
def fantasy():
    return """
<h3>Korean Fantasy Dramas</h3>•
Goblin<br>•
Alchemy of Souls<br>•
Hotel del Luna<br>•
My Demon<br>•
Moving<br>•
The Uncanny Counter<br>•
Tale of the Nine Tailed<br>•
A Korean Odyssey<br>•
See You in My 19th Life<br>•
Twinkling Watermelon<br><br>
<h3>Hollywood Fantasy Series</h3>•
Game of Thrones<br>•
House of the Dragon<br>•
The Lord of the Rings: The Rings of Power<br>•
The Witcher<br>•
Shadow and Bone<br>•
The Sandman<br>•
His Dark Materials<br>•
Merlin<br>•
The Wheel of Time<br>•
Arcane<br><br>
<h3>Fantasy + Adventure</h3>•
Avatar: The Last Airbender<br>•
Sweet Tooth<br>•
Locke & Key<br>•
Once Upon a Time<br>•
Carnival Row<br>•
Fate: The Winx Saga<br>•
The Shannara Chronicles<br>•
Wednesday<br>•
Lucifer<br>•
Supernatural<br><br>
<h3>Top 10 Fantasy Series Overall</h3>•
Game of Thrones<br>•
House of the Dragon<br>•
The Witcher<br>•
The Sandman<br>•
Arcane<br>•
Goblin<br>•
Alchemy of Souls<br>•
Hotel del Luna<br>•
Moving<br>•
The Lord of the Rings: The Rings of Power
    """
@app.route("/kdrama")
def kdrama():
    return """
Crash Landing on You<br>•
Goblin<br>•
Descendants of the Sun<br>•
Vincenzo<br>•
Itaewon Class<br>•
Extraordinary Attorney Woo<br>•
Hospital Playlist<br>•
Reply 1988<br>•
Twenty-Five Twenty-One<br>•
Business Proposal<br>•
Kingdom<br>•
Sweet Home<br>•
All of Us Are Dead<br>•
The Glory<br>•
Squid Game<br>•
My Name<br>•
Flower of Evil<br>•
Signal<br>•
Mouse<br>•
Beyond Evil<br>•
Moving<br>•
Alchemy of Souls<br>•
Mr. Queen<br>•
Mr. Sunshine<br>•
Moon Lovers: Scarlet Heart Ryeo<br>•
Healer<br>•
While You Were Sleeping<br>•
Strong Woman Do Bong Soon<br>•
Weightlifting Fairy Kim Bok-joo<br>•
Hometown Cha-Cha-Cha<br>•
Our Beloved Summer<br>•
Love Next Door<br>•
Queen of Tears<br>•
Marry My Husband<br>•
A Shop for Killers<br>•
Weak Hero Class 1<br>•
The Uncanny Counter<br>•
Taxi Driver<br>•
Big Mouth<br>•
Reborn Rich<br>•
    """
@app.route("/motivation")
def motivation():
    return """
    <body style="
        text-align:center;
        font-family:Arial;
        background-color:#f5f5f5;
         ">
    <h1>Motivational Quotes</h1>
   •  Believe you can and you're halfway there.     — Theodore Roosevelt
    <br>
   •  The only limit to our realization of tomorrow will be our doubts of today.     — Franklin D. Roosevelt
    <br>
   •   It always seems impossible until it's done.     — Nelson Mandela
    <br>
   •   Keep your face always toward the sunshine—and shadows will fall behind you.     — Walt Whitman
    <br>
   •   Positivity brings peace of mind which relaxes your body and in turn helps you achieve more.     — Unknown
    <br>
   •   Act as if what you do makes a difference. It does.     — William James
    <br>
   •   Success is not final, failure is not fatal: It is the courage to continue that counts.     — Winston Churchill
    <br>
   •   Turn your wounds into wisdom.     — Oprah Winfrey
    <br>
   •   The most wasted of all days is one without laughter.     — e.e. cumming
    <br>
   •   In the middle of every difficulty lies opportunity.     — Albert Einstein
    <br>
    •  If an artist falls in love with you, you can never die.
    <br>
   •   No one is in charge of your happiness but you.     — Unknown
    <br>
   •   Optimism is the faith that leads to achievement.     — Helen Keller
    <br>
   •   With the new day comes new strength and new thoughts.     — Eleanor Roosevelt
    <br>
   •   Happiness is not something ready made. It comes from your own actions.     — Dalai Lama
    <br>
   •   You are never too old to set another goal or to dream a new dream.     — C.S. Lewis
    <br>
   •   We may encounter many defeats but we must not be defeated.     — Maya Angelou
    <br>
   •   It is during our darkest moments that we must focus to see the light.     — Aristotle
    <br>
   •Yesterday is not ours to recover, but tomorrow is ours to win or lose.     — Lyndon B. Johnson
    <br>
   •The only person you are destined to become is the person you decide to be.     — Ralph Waldo Emerson
    <br>
   •Be the change that you wish to see in the world.     — Mahatma Gandhi
    """
@app.route("/jokes")
def jokes():
    return """
    <h1>Jokes</h1>
    <br>★ Teacher: Why are you late? Student: Because of the sign. Teacher: What sign? Student: 'School Ahead   Go Slow!' 😆   

    <br>★ Why do programmers prefer dark mode? Because light attracts bugs! 😂   

    <br>★ అమ్మ: చదువుతున్నావా? కొడుకు: అవును అమ్మ. అమ్మ: మరి ఫోన్ ఎందుకు చేతిలో ఉంది? కొడుకు: డిజిటల్ చదువు! 😄   

    <br>★ Why don't scientists trust atoms? Because they make up everything! 🤣   

    <br>★ Teacher: What is your father's name? Student: Daddy. 😆   

    <br>★ ఏనుగు కంప్యూటర్ ఎందుకు కొనలేదు? Mouse చూసి భయపడింది! 🐘😂   

    <br>★ Why was the math book sad? It had too many problems! 📚😅   

    <br>★ విద్యార్థి: సార్   పరీక్షలో సున్నా వచ్చింది. సార్: ఎందుకు? విద్యార్థి: ప్రశ్నలన్నీ కొత్తవి సార్! 😆   

    <br>★ Why did the computer go to the doctor? It caught a virus! 💻🤣   

    <br>★ అమ్మ: గది శుభ్రం చేశావా? కొడుకు: అవును. అమ్మ: మరి చెత్త? కొడుకు: మంచం కింద దాచాను! 😂   

    <br>★ Why was the computer cold? It left its Windows open! 🪟😄   

    <br>★ Teacher: Name a bird that cannot fly. Student: Dead bird! 😂   

    <br>★ పిల్లి: నాకు Wi-Fi password చెప్పు. యజమాని: ఎందుకు? పిల్లి: MeowTube చూడాలి! 🐱😆   

    <br>★ Why did the bicycle fall over? Because it was two-tired! 🚲🤣   

    <br>★ Teacher: What is 2+2? Student: Easy. Teacher: Then answer. Student: That's the difficult part! 😄   

    <br>★ కోడి రోడ్డు ఎందుకు దాటింది? ఆ ప్రశ్నకు సమాధానం తెలుసుకోవడానికి! 🐔😂   

    <br>★ Why can't a skeleton fight? Because it doesn't have the guts! 💀😆   

    <br>★ Teacher: Who invented homework? Student: My enemy! 🤣   

    <br>★ అమ్మ: ఫోన్ వదిలి చదువు. కొడుకు: ఫోన్‌లోనే చదువుతున్నాను. అమ్మ: ఏం చదువుతున్నావు? కొడుకు: మీ మెసేజ్‌లు! 😄   

    <br>★ Why did the student eat his homework? Because the teacher said it was a piece of cake! 🎂😂   

    <br>★ Teacher: Tell me a sentence with 'I'. Student: I is... Teacher: No   say 'I am'. Student: Okay   I am the ninth letter! 🤣   

    <br>★ పరీక్షలో విద్యార్థి: సార్   ఈ ప్రశ్నకు జవాబు దేవుడికే తెలుసు. సార్: మరి నువ్వు ఎందుకు రాయలేదు? విద్యార్థి: నేను దేవుడు కాదు సార్! 😆   

    <br>★ Why do Java developers wear glasses? Because they don't C#! 🤓😂   

    <br>★ Teacher: What is your weakness? Student: Honesty. Teacher: I don't think honesty is a weakness. Student: I don't care what you think! 🤣   

    <br>★ కంప్యూటర్: నాకు ఆకలిగా ఉంది. యజమాని: ఎందుకు? కంప్యూటర్: చాలా cookies delete చేశావు! 🍪😄   

    <br>★ Why did the scarecrow win an award? Because he was outstanding in his field! 🌾😂   

    <br>★ Teacher: Why are you talking during my lesson? Student: Because I don't want to interrupt you! 😆   

    <br>★ అమ్మ: పాలు తాగావా? కొడుకు: అవును. అమ్మ: గ్లాస్ ఖాళీగా లేదు కదా? కొడుకు: పాలు మాత్రమే తాగాను! 😂   

    <br>★ Why was six afraid of seven? Because seven eight nine! 🤣   

    <br>★ Friend: Do you know swimming? Me: Yes. Friend: Then why are you drowning? Me: This is practical   not theory! 😄 
    """
@app.route("/funfacts")
def funfacts():
    return """
<h1>Fun facts</h1>
        <br>★Honey never spoils.
        <br>★Octopuses have three hearts. 
        <br>★Sharks existed before dinosaurs.
        <br>★Bananas are berries.
        <br>★Koalas sleep up to 20 hours a day. 
        <br>★The Moon is moving away from Earth
        <br>★A blue whale's heart is as big as a small car. 
        <br>★Lightning is hotter than the Sun's surface.
         <br>★Honey never spoils.   
         <br>★Octopuses have three hearts.   
         <br>★Sharks existed before dinosaurs.   
         <br>★Bananas are berries.   
         <br>★A day on Venus is longer than a year on Venus.   
         <br>★Koalas sleep up to 20 hours a day.   
         <br>★The Moon moves away from Earth by about 3.8 cm each year.   
         <br>★A blue whale's heart can weigh over 180 kg.   
         <br>★Sloths can hold their breath longer than dolphins.   
         <br>★The Eiffel Tower grows taller in summer.   
         <br>★Lightning is hotter than the Sun's surface.   
         <br>★Cows have best friends.   
         <br>★A group of flamingos is called a flamboyance.   
         <br>★There are more stars than grains of sand on Earth.   
         <br>★Wombat poop is cube-shaped.   
         <br>★An ostrich's eye is bigger than its brain.   
         <br>★Sea otters hold hands while sleeping.   
         <br>★Butterflies taste with their feet.   
         <br>★A crocodile cannot stick out its tongue.   
         <br>★The shortest war lasted 38 minutes.   
         <br>★Some turtles can breathe through their bottoms.   
         <br>★The human nose can detect over a trillion scents.   
         <br>★Cats sleep for about 70% of their lives.   
         <br>★A snail can sleep for up to three years.   
         <br>★The fingerprints of a koala resemble human fingerprints.   
         <br>★A cloud can weigh over a million pounds.   
         <br>★The heart beats about 100,000 times per day.   
         <br>★The world's largest desert is Antarctica.   
         <br>★Hot water can freeze faster than cold water.   
         <br>★A bolt of lightning contains enough energy to toast 100,000 slices of bread.   
         <br>★Jellyfish have existed for over 500 million years.   
         <br>★The average person walks enough in a lifetime to circle Earth several times.   
         <br>★A giraffe's tongue can be over 45 cm long.   
         <br>★Penguins propose with pebbles.   
         <br>★Some bamboo species can grow nearly a meter in a day.   
         <br>★A day on Mercury lasts about 176 Earth days.   
         <br>★The ocean contains about 97% of Earth's water.   
         <br>★A sneeze can travel over 150 km/h.   
         <br>★Dragonflies can fly in all directions.   
         <br>★The human body contains enough iron to make a small nail.   
         <br>★The longest hiccup attack lasted 68 years.   
         <br>★There are more possible chess games than atoms in the observable universe.   
         <br>★An apple floats because it is about 25% air.   
         <br>★The unicorn is the national animal of Scotland.   
         <br>★A group of crows is called a murder.   ]
    """
@app.route("/animes")
def animes():
    return """
    ✦Attack on Titan<br>✦
Bleach<br>✦
Cowboy Bebop<br>✦
Death Note<br>✦
Dragon Ball Z<br>✦
Fullmetal Alchemist: Brotherhood<br>✦
Hunter x Hunter<br>✦
My Hero Academia<br>✦
Naruto<br>✦
Neon Genesis Evangelion<br>✦
One Piece<br>✦
One Punch Man<br>✦
Sailor Moon<br>✦
Sword Art Online<br>✦
Tokyo Ghoul<br>✦
Demon Slayer: Kimetsu no Yaiba<br>✦
Jujutsu Kaisen<br>✦
Black Clover<br>✦
Fairy Tail<br>✦
Attack on Titan
    """
@app.route("/action")
def action():
    return """
50 Action Movies to Watch<br>✦
John Wick<br>✦
John Wick: Chapter 2<br>✦
John Wick: Chapter 3 – Parabellum<br>✦
John Wick: Chapter 4<br>✦
Die Hard<br>✦
The Matrix<br>✦
Mad Max: Fury Road<br>✦
Terminator 2: Judgment Day<br>✦
Speed<br>✦
Face/Off<br>✦
Mission: Impossible<br>✦
Mission: Impossible II<br>✦
Mission: Impossible III<br>✦
Mission: Impossible – Ghost Protocol<br>✦
Mission: Impossible – Rogue Nation<br>✦
Mission: Impossible – Fallout<br>✦
Top Gun: Maverick<br>✦
Extraction<br>✦
Extraction 2<br>✦
Nobody<br>✦
The Dark Knight<br>✦
Batman Begins<br>✦
The Dark Knight Rises<br>✦
Logan<br>✦
Captain America: The Winter Soldier<br>✦
Avengers: Infinity War<br>✦
Avengers: Endgame<br>✦
Spider-Man: No Way Home<br>✦
Black Panther<br>✦
Shang-Chi and the Legend of the Ten Rings<br>✦
The Raid<br>✦
The Raid 2<br>✦
Ip Man<br>✦
Ip Man 2<br>✦
Police Story<br>✦
Rush Hour<br>✦
Enter the Dragon<br>✦
Crouching Tiger, Hidden Dragon<br>✦
Kill Bill: Vol. 1<br>✦
Kill Bill: Vol. 2<br>✦
RRR<br>✦
Vikram<br>✦
KGF: Chapter 1<br>✦
KGF: Chapter 2<br>✦
Salaar: Part 1 – Ceasefire<br>✦
Pushpa: The Rise<br>✦
Singham<br>✦
War<br>✦
Pathaan<br>✦
Animal<br>
    """
@app.route("/family")
def family():
    return """  
The Lion King<br>✦
Finding Nemo<br>✦
Finding Dory<br>✦
Toy Story<br>✦
Toy Story 2<br>✦
Toy Story 3<br>✦
Toy Story 4<br>✦
Up<br>✦
Inside Out<br>✦
Inside Out 2<br>✦
Coco<br>✦
Moana<br>✦
Frozen<br>✦
Frozen II<br>✦
Encanto<br>✦
Ratatouille<br>✦
Wall-E<br>✦
The Incredibles<br>✦
Incredibles 2<br>✦
Cars<br>✦
Cars 2<br>✦
Cars 3<br>✦
Monsters, Inc.<br>✦
Monsters University<br>✦
Brave<br>✦
Tangled<br>✦
Big Hero 6<br>✦
Zootopia<br>✦
Luca<br>✦
Soul<br>✦
Harry Potter and the Sorcerer's Stone<br>✦
Harry Potter and the Chamber of Secrets<br>✦
The Chronicles of Narnia: The Lion, the Witch and the Wardrobe<br>✦
Paddington<br>✦
Paddington 2<br>✦
Peter Rabbit<br>✦
Night at the Museum<br>✦
Jumanji<br>✦
Jumanji: Welcome to the Jungle<br>✦
Jumanji: The Next Level<br>✦
The Sound of Music<br>✦
Home Alone<br>✦
Home Alone 2: Lost in New York<br>✦
The Parent Trap<br>✦
Wonder<br>✦
The Karate Kid<br>✦
The Karate Kid<br>✦
Akeelah and the Bee<br>✦
Babe<br>✦
The Secret Garden<br>
Top 10 Family Movies<br>
⭐ Coco<br>
⭐ Up<br>
⭐ The Lion King<br>
⭐ Finding Nemo<br>
⭐ Inside Out<br>
⭐ Encanto<br>
⭐ Wonder<br>
⭐ Home Alone<br>
⭐ Paddington 2<br>
⭐ Big Hero 6<br>
    """
@app.route("/scifi")
def scifi():
    return """
Here are 50 must-watch Sci-Fi movies from different eras and styles:<br>✦
2001: A Space Odyssey<br>✦
Star Wars<br>✦
Alien<br>✦
Blade Runner<br>✦
The Terminator<br>✦
Aliens<br>✦
Predator<br>✦
Akira<br>✦
Total Recall<br>✦
Terminator 2: Judgment Day<br>✦
Jurassic Park<br>✦
The Fifth Element<br>✦
Gattaca<br>✦
The Matrix<br>✦
A.I. Artificial Intelligence<br>✦
Minority Report<br>✦
Eternal Sunshine of the Spotless Mind<br>✦
Primer<br>✦
Children of Men<br>✦
Sunshine<br>✦
WALL-E<br>✦
Moon<br>✦
Inception<br>✦
Rise of the Planet of the Apes<br>✦
Looper<br>✦
Her<br>✦
Snowpiercer<br>✦
Edge of Tomorrow<br>✦
Interstellar<br>✦
Ex Machina<br>✦
The Martian<br>✦
Arrival<br>✦
Rogue One<br>✦
Blade Runner 2049<br>✦
Annihilation<br>✦
Ready Player One<br>✦
Alita: Battle Angel<br>✦
Tenet<br>✦
Dune<br>✦
The Tomorrow War<br>✦
Everything Everywhere All at Once<br>✦
Avatar: The Way of Water<br>✦
The Creator<br>✦
Dune: Part Two<br>✦
District 9<br>✦
Contact<br>✦
The Thing<br>✦
Close Encounters of the Third Kind<br>✦
Forbidden Planet<br>✦
Under the Skin<br>✦
    """
@app.route("/horror")
def horror():
    return """
    A Nightmare on Elm Street<•
Alien<br>•
Amityville Horror<br>•
Anaconda<br>•
Annabelle<br>•
Basket Case<br>•
Blair Witch<br>•
Candyman<br>•
Carrie<br>•
Cube<br>•
Darkman<br>•
Dead Snow<br>•
Death Note<br>•
Deep Blue Sea<br>•
Evil Dead<br>•
Exorcist<br>•
Final Destination<br>•
Friday the 13th<br>•
Fright Night<br>•
From Dusk Till Dawn<br>•
Ginger Snaps<br>•
Gremlins<br>•
Halloween<br>•
Hellraiser<br>•
Hostel<br>•
House of 1000 Corpses<br>•
I Know What You Did Last Summer<br>•
Insidious<br>•
It<br>•
Jaws<br>•
Jeepers Creepers<br>•
Ju-On<br>•
Leprechaun<br>•
Maniac Cop<br>•
Night of the Demons<br>•
Paranormal Activity<br>•
Pet Sematary<br>•
Phantasm<br>•
Poltergeist<br>•
Predator<br>•
Prom Night<br>•
Psycho<br>•
Pumpkinhead<br>•
Puppet Master<br>•
Purge<br>•
Re-Animator<br>•
Resident Evil<br>•
Ring<br>•
Saw<br>•
Scream<br>•
Silent Hill<br>•
Sinister<br>•
Sleepaway Camp<br>•
Slumber Party Massacre<br>•
Species<br>•
Tales from the Crypt<br>•
Tales from the Hood<br><br>•
Terminator<br><br>•
V/H/S<br>•
Wishmaster<br>•
Wolf Creek<br>•
Wrong Turn<br>•
Zombieland•<br>
    """
@app.route("/comedy")
def comedy():
    return """
    •Airplane!<br>
Anchorman: The Legend of Ron Burgundy<br>•
Austin Powers: International Man of Mystery<br>•
Back to the Future<br>•
Beverly Hills Cop<br>•
Happy Gilmore<br>•
Hot Fuzz<br>•
Juno<br>•
Kingsman: The Secret Service<br>•
Legally Blonde<br>•
Liar Liar<br>•
Little Miss Sunshine<br>•
Mean Girls<br>•
Meet the Parents<br>•
Monty Python and the Holy Grail<br>•
Napoleon Dynamite<br>•
National Lampoon's Animal House<br>•
National Lampoon's Christmas Vacation<br>•
O Brother, Where Art Thou?<br>•
Office Space<br>•
Old School<br>•
Planes, Trains and Automobiles<br>•
Raising Arizona<br>•
Rush Hour<br>•
School of Rock<br>•
Shaun of the Dead<br>•
Shrek<br>•
Some Like It Hot<br>•
Spaceballs<br>•
Step Brothers<br>•
Superbad<br>•
The 40-Year-Old Virgin<br>•
The Big Lebowski<br>•
The Blues Brothers<br>•
The Breakfast Club<br>•
The Grand Budapest Hotel<br>•
The Hangover<br>•
When Harry Met Sally...<br>•
Young Frankenstein<br>•
Zoolander<br>
    """
@app.route("/study")
def study():
    return"""
    <h1>Study</h1>
    <a href=/tips>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Study Tips</button>
    </a><br>
    <a href=/motivation>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Motivation</button>
    </a><br>
    <a href=/quiz>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Quiz</button>
    </a><br>
    <a href=/programmingtips>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Programming Tips</button>
    </a><br>
    <a href=/time>
        <button style="
        width:250px;
        height:40px;
        font-size:15px;
        margin:10px"
        >Time Management</button>
    </a><br>
    """
@app.route("/tips")
def tips():
    return"""
<h1>Study tips</h1>   
1. Follow the Pomodoro Technique (25 min study + 5 min break  <br><br>
       2. Make short notes.    <br><br>
       3. Revise daily.    <br><br>
       4. Practice previous questions.    
    """

@app.route("/time")
def time():
    return """
    <h1>Time Management</h1>
        • Create a daily schedule.  <br><br>  
        • Prioritize important tasks.    <br><br>
        • Avoid social media while studying.    
    """
@app.route("/programmingtips")
def programmingtips():
    return"""
    <h1>Programming tips</h1>
• Practice coding every day.<br><br>
• Build small projects..<br><br>
 • Learn Git and GitHub..<br><br>
 • Solve coding problems regularly.
    """
@app.route("/fitness")
def fitness():
    return """

      <h1>FITNESS TIPS </h1>
      1. Drink 2-3 liters of water daily.  <br><br>
      2. Walk at least 8,000-10,000 steps every day.  <br><br>
      3. Exercise for 20-30 minutes daily.  <br><br>
      4. Eat protein-rich foods like eggs, soya chunks, and dal.  <br><br>
  5. Get 7-9 hours of sleep every night.  <br><br>
          6. Avoid sugary drinks and junk food.  <br><br>
          7. Eat more fruits and vegetables.  <br><br>
          8. Take the stairs instead of the elevator.  <br><br>
          9. Stretch before and after workouts.  <br><br>
          10. Stay consistent with your fitness routine.  <br><br>
  11. Avoid skipping meals.  <br><br>
          12. Reduce screen time before bed.  <br><br>
          13. Maintain good posture while sitting.  <br><br>
          14. Take short walking breaks while studying.  <br><br>
          15. Focus on progress, not perfection.  <br><br>
  16. Do strength training 2-3 times per week.  <br><br>
          17. Avoid late-night snacking.  <br><br>
          18. Eat slowly and mindfully.  <br><br>
          19. Set realistic fitness goals.  <br><br>
          20. Never give up on your fitness journey!  <br><br>
    """
@app.route("/cooking")
def cooking():
    return render_template("recipe.html")
@app.route("/budget")
def budget():
    return render_template("budget_planner.html")
@app.route("/calculator")
def calculator():
    return render_template("calculator-1.html")
app.run(host="0.0.0.0",port=5000,debug=True)