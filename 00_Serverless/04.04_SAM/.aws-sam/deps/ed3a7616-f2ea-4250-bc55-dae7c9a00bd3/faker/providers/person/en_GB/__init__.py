from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = (
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}-{{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}}",
    )

    formats_male = (
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}-{{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
    )

    formats = formats_female + formats_male

    # Names from
    # http://webarchive.nationalarchives.gov.uk/20160105160709/http://ons.gov.uk/ons/publications/re-reference-tables.html?edition=tcm%3A77-243767

    first_names_male = (
        "David",
        "Paul",
        "Christopher",
        "Thomas",
        "John",
        "Mark",
        "James",
        "Stephen",
        "Andrew",
        "Jack",
        "Michael",
        "Daniel",
        "Peter",
        "Richard",
        "Matthew",
        "Robert",
        "Ryan",
        "Joshua",
        "Alan",
        "Ian",
        "Simon",
        "Luke",
        "Samuel",
        "Jordan",
        "Anthony",
        "Adam",
        "Lee",
        "Alexander",
        "William",
        "Kevin",
        "Darren",
        "Benjamin",
        "Philip",
        "Gary",
        "Joseph",
        "Brian",
        "Steven",
        "Liam",
        "Keith",
        "Martin",
        "Jason",
        "Jonathan",
        "Jake",
        "Graham",
        "Nicholas",
        "Craig",
        "George",
        "Colin",
        "Neil",
        "Lewis",
        "Nigel",
        "Oliver",
        "Timothy",
        "Stuart",
        "Kenneth",
        "Raymond",
        "Jamie",
        "Nathan",
        "Geoffrey",
        "Connor",
        "Terence",
        "Trevor",
        "Adrian",
        "Harry",
        "Malcolm",
        "Scott",
        "Callum",
        "Wayne",
        "Aaron",
        "Barry",
        "Ashley",
        "Bradley",
        "Patrick",
        "Gareth",
        "Jacob",
        "Sean",
        "Kieran",
        "Derek",
        "Carl",
        "Dean",
        "Charles",
        "Sam",
        "Shaun",
        "Ben",
        "Roger",
        "Mohammed",
        "Leslie",
        "Ronald",
        "Kyle",
        "Clive",
        "Edward",
        "Antony",
        "Jeremy",
        "Justin",
        "Jeffrey",
        "Christian",
        "Roy",
        "Karl",
        "Alex",
        "Gordon",
        "Dominic",
        "Joe",
        "Marc",
        "Reece",
        "Dennis",
        "Russell",
        "Gavin",
        "Rhys",
        "Phillip",
        "Allan",
        "Robin",
        "Charlie",
        "Gerald",
        "Ross",
        "Francis",
        "Eric",
        "Julian",
        "Bernard",
        "Dale",
        "Donald",
        "Damian",
        "Frank",
        "Shane",
        "Cameron",
        "Norman",
        "Duncan",
        "Louis",
        "Frederick",
        "Tony",
        "Howard",
        "Conor",
        "Douglas",
        "Garry",
        "Elliot",
        "Marcus",
        "Arthur",
        "Vincent",
        "Max",
        "Mathew",
        "Abdul",
        "Henry",
        "Martyn",
        "Ricky",
        "Leonard",
        "Lawrence",
        "Glen",
        "Mitchell",
        "Gerard",
        "Gregory",
        "Iain",
        "Billy",
        "Bryan",
        "Joel",
        "Clifford",
        "Josh",
        "Leon",
        "Stewart",
        "Mohammad",
        "Dylan",
        "Graeme",
        "Terry",
        "Guy",
        "Elliott",
        "Stanley",
        "Danny",
        "Brandon",
        "Victor",
        "Toby",
        "Hugh",
        "Mohamed",
        "Brett",
        "Albert",
        "Tom",
        "Declan",
        "Maurice",
        "Glenn",
        "Leigh",
        "Denis",
        "Damien",
        "Bruce",
        "Jay",
        "Owen",
    )

    first_names_female = (
        "Susan",
        "Sarah",
        "Rebecca",
        "Linda",
        "Julie",
        "Claire",
        "Laura",
        "Lauren",
        "Christine",
        "Karen",
        "Nicola",
        "Gemma",
        "Jessica",
        "Margaret",
        "Jacqueline",
        "Emma",
        "Charlotte",
        "Janet",
        "Deborah",
        "Lisa",
        "Hannah",
        "Patricia",
        "Tracey",
        "Joanne",
        "Sophie",
        "Carol",
        "Jane",
        "Michelle",
        "Victoria",
        "Amy",
        "Elizabeth",
        "Helen",
        "Samantha",
        "Emily",
        "Mary",
        "Diane",
        "Rachel",
        "Anne",
        "Sharon",
        "Ann",
        "Tracy",
        "Amanda",
        "Jennifer",
        "Chloe",
        "Angela",
        "Louise",
        "Katie",
        "Lucy",
        "Barbara",
        "Alison",
        "Sandra",
        "Caroline",
        "Clare",
        "Kelly",
        "Bethany",
        "Gillian",
        "Natalie",
        "Jade",
        "Pauline",
        "Megan",
        "Elaine",
        "Alice",
        "Lesley",
        "Catherine",
        "Hayley",
        "Pamela",
        "Danielle",
        "Holly",
        "Wendy",
        "Abigail",
        "Valerie",
        "Olivia",
        "Jean",
        "Dawn",
        "Donna",
        "Stephanie",
        "Leanne",
        "Kathleen",
        "Natasha",
        "Denise",
        "Sally",
        "Katherine",
        "Georgia",
        "Maureen",
        "Maria",
        "Zoe",
        "Judith",
        "Kerry",
        "Debra",
        "Melanie",
        "Stacey",
        "Eleanor",
        "Paula",
        "Shannon",
        "Sheila",
        "Joanna",
        "Paige",
        "Janice",
        "Lorraine",
        "Georgina",
        "Lynn",
        "Andrea",
        "Suzanne",
        "Nicole",
        "Yvonne",
        "Chelsea",
        "Lynne",
        "Anna",
        "Kirsty",
        "Shirley",
        "Alexandra",
        "Marion",
        "Beverley",
        "Melissa",
        "Rosemary",
        "Kimberley",
        "Carole",
        "Fiona",
        "Kate",
        "Joan",
        "Marie",
        "Jenna",
        "Marilyn",
        "Jodie",
        "June",
        "Grace",
        "Mandy",
        "Rachael",
        "Lynda",
        "Tina",
        "Kathryn",
        "Molly",
        "Jayne",
        "Amber",
        "Marian",
        "Jasmine",
        "Brenda",
        "Sara",
        "Kayleigh",
        "Teresa",
        "Harriet",
        "Julia",
        "Ashleigh",
        "Heather",
        "Kim",
        "Ruth",
        "Jemma",
        "Carly",
        "Leah",
        "Eileen",
        "Francesca",
        "Naomi",
        "Hilary",
        "Abbie",
        "Sylvia",
        "Katy",
        "Irene",
        "Cheryl",
        "Rosie",
        "Dorothy",
        "Aimee",
        "Vanessa",
        "Ellie",
        "Frances",
        "Sian",
        "Josephine",
        "Gail",
        "Jill",
        "Lydia",
        "Joyce",
        "Charlene",
        "Hollie",
        "Hazel",
        "Annette",
        "Bethan",
        "Amelia",
        "Beth",
        "Rita",
        "Geraldine",
        "Diana",
        "Lindsey",
        "Carolyn",
    )

    first_names = first_names_male + first_names_female

    last_names = OrderedDict(
        (
            ("Savage", 0.04),
            ("Winter", 0.03),
            ("Metcalfe", 0.03),
            ("Harper", 0.06),
            ("Burgess", 0.06),
            ("Bailey", 0.15),
            ("Potts", 0.03),
            ("Boyle", 0.03),
            ("Brown", 0.51),
            ("Jennings", 0.05),
            ("Payne", 0.09),
            ("Day", 0.09),
            ("Holland", 0.07),
            ("Higgins", 0.05),
            ("Rhodes", 0.04),
            ("Hancock", 0.04),
            ("Howells", 0.03),
            ("Fowler", 0.04),
            ("Sims", 0.03),
            ("Thomas", 0.35),
            ("Parker", 0.17),
            ("Bentley", 0.04),
            ("Barnett", 0.05),
            ("Manning", 0.03),
            ("Collier", 0.03),
            ("Holloway", 0.03),
            ("Hartley", 0.04),
            ("George", 0.05),
            ("Tomlinson", 0.04),
            ("Howard", 0.09),
            ("Long", 0.06),
            ("Farmer", 0.03),
            ("Collins", 0.15),
            ("Rice", 0.03),
            ("Townsend", 0.04),
            ("Rees", 0.07),
            ("Bruce", 0.03),
            ("Hammond", 0.05),
            ("Ford", 0.09),
            ("Tucker", 0.05),
            ("Wallis", 0.03),
            ("Hamilton", 0.06),
            ("Ferguson", 0.04),
            ("Hooper", 0.03),
            ("Francis", 0.07),
            ("Reeves", 0.04),
            ("Barlow", 0.04),
            ("Short", 0.04),
            ("Cunningham", 0.05),
            ("Hopkins", 0.06),
            ("Nicholson", 0.06),
            ("Archer", 0.04),
            ("Green", 0.25),
            ("Glover", 0.04),
            ("Gibson", 0.09),
            ("Spencer", 0.08),
            ("Warner", 0.04),
            ("Webb", 0.12),
            ("Whitehouse", 0.03),
            ("Dean", 0.06),
            ("Griffiths", 0.16),
            ("Clark", 0.2),
            ("Hardy", 0.05),
            ("Iqbal", 0.03),
            ("Baldwin", 0.04),
            ("O'Neill", 0.06),
            ("Blake", 0.05),
            ("Lees", 0.03),
            ("Harvey", 0.1),
            ("Clarke", 0.24),
            ("Daniels", 0.04),
            ("Browne", 0.03),
            ("Macdonald", 0.04),
            ("Kirk", 0.04),
            ("Khan", 0.14),
            ("Davidson", 0.05),
            ("Dale", 0.04),
            ("Sanders", 0.04),
            ("Wilkins", 0.04),
            ("Connor", 0.03),
            ("Daly", 0.03),
            ("Lane", 0.06),
            ("Kennedy", 0.06),
            ("Bray", 0.03),
            ("Burrows", 0.04),
            ("Hayes", 0.07),
            ("Wyatt", 0.03),
            ("Gould", 0.03),
            ("Dyer", 0.03),
            ("Nash", 0.05),
            ("Bryan", 0.03),
            ("Pope", 0.03),
            ("Fraser", 0.04),
            ("Steele", 0.03),
            ("Walsh", 0.09),
            ("Wade", 0.04),
            ("Marsden", 0.03),
            ("Humphries", 0.03),
            ("O'Brien", 0.08),
            ("Thompson", 0.28),
            ("Lord", 0.03),
            ("Coleman", 0.06),
            ("Jarvis", 0.04),
            ("Noble", 0.03),
            ("Williamson", 0.06),
            ("Carpenter", 0.03),
            ("Gardner", 0.06),
            ("Farrell", 0.04),
            ("Clayton", 0.05),
            ("Akhtar", 0.05),
            ("Gallagher", 0.05),
            ("Skinner", 0.04),
            ("Birch", 0.04),
            ("Kay", 0.04),
            ("Barrett", 0.07),
            ("Bates", 0.06),
            ("Lucas", 0.04),
            ("O'Connor", 0.06),
            ("Chamberlain", 0.03),
            ("Chapman", 0.12),
            ("Ryan", 0.08),
            ("Thorpe", 0.04),
            ("Lawson", 0.04),
            ("Howell", 0.04),
            ("Martin", 0.23),
            ("Kelly", 0.16),
            ("Dobson", 0.04),
            ("Stevens", 0.1),
            ("Brennan", 0.04),
            ("Lloyd", 0.11),
            ("Quinn", 0.05),
            ("Morton", 0.04),
            ("Wilson", 0.35),
            ("Barnes", 0.11),
            ("Henry", 0.03),
            ("Smith", 1.15),
            ("Pritchard", 0.05),
            ("Phillips", 0.18),
            ("Dixon", 0.1),
            ("Sharpe", 0.03),
            ("Robertson", 0.07),
            ("White", 0.27),
            ("Bird", 0.06),
            ("Abbott", 0.04),
            ("Kirby", 0.04),
            ("Hussain", 0.11),
            ("Barber", 0.05),
            ("Harris", 0.25),
            ("Doyle", 0.05),
            ("Jordan", 0.05),
            ("Burns", 0.06),
            ("Hodgson", 0.06),
            ("Atkins", 0.04),
            ("Stokes", 0.05),
            ("Rogers", 0.12),
            ("Parkes", 0.03),
            ("Brookes", 0.04),
            ("Herbert", 0.03),
            ("Gordon", 0.05),
            ("Kemp", 0.05),
            ("Webster", 0.07),
            ("Sinclair", 0.03),
            ("McLean", 0.03),
            ("Saunders", 0.09),
            ("Stephens", 0.05),
            ("Newton", 0.07),
            ("Potter", 0.05),
            ("Storey", 0.03),
            ("Stanley", 0.04),
            ("Turnbull", 0.03),
            ("Duncan", 0.03),
            ("Rose", 0.08),
            ("Mills", 0.11),
            ("Sheppard", 0.03),
            ("Butcher", 0.03),
            ("Fry", 0.03),
            ("Ross", 0.06),
            ("Shepherd", 0.06),
            ("Goodwin", 0.05),
            ("Holt", 0.05),
            ("Haynes", 0.04),
            ("Cook", 0.15),
            ("Ward", 0.21),
            ("Godfrey", 0.03),
            ("Stone", 0.07),
            ("Dodd", 0.04),
            ("Parsons", 0.07),
            ("Ingram", 0.03),
            ("Nixon", 0.03),
            ("Evans", 0.39),
            ("Hargreaves", 0.03),
            ("Owen", 0.11),
            ("Chan", 0.03),
            ("Connolly", 0.03),
            ("Charlton", 0.03),
            ("Middleton", 0.04),
            ("Hyde", 0.03),
            ("Patel", 0.24),
            ("Owens", 0.03),
            ("Lamb", 0.04),
            ("Palmer", 0.11),
            ("Cooper", 0.22),
            ("McCarthy", 0.06),
            ("Black", 0.04),
            ("Dickinson", 0.04),
            ("Gilbert", 0.05),
            ("Leach", 0.03),
            ("North", 0.03),
            ("Byrne", 0.06),
            ("Frost", 0.05),
            ("Simmons", 0.04),
            ("Matthews", 0.11),
            ("Alexander", 0.04),
            ("Ahmed", 0.1),
            ("Gibbons", 0.03),
            ("Stevenson", 0.05),
            ("Rowley", 0.03),
            ("Miles", 0.05),
            ("Hanson", 0.03),
            ("Bolton", 0.03),
            ("Craig", 0.03),
            ("Ali", 0.12),
            ("Carroll", 0.04),
            ("Allan", 0.03),
            ("Sanderson", 0.03),
            ("Fletcher", 0.1),
            ("Burton", 0.08),
            ("Oliver", 0.07),
            ("Davison", 0.04),
            ("Douglas", 0.04),
            ("Field", 0.04),
            ("Pickering", 0.03),
            ("Pugh", 0.04),
            ("Rowe", 0.05),
            ("Mahmood", 0.03),
            ("Sykes", 0.03),
            ("Crawford", 0.03),
            ("Williams", 0.66),
            ("Parkin", 0.03),
            ("Patterson", 0.04),
            ("Power", 0.03),
            ("Price", 0.17),
            ("Murphy", 0.14),
            ("Hale", 0.03),
            ("Nicholls", 0.06),
            ("Hall", 0.25),
            ("Jones", 0.94),
            ("Hughes", 0.26),
            ("Stephenson", 0.05),
            ("Morley", 0.04),
            ("Knight", 0.11),
            ("Kerr", 0.03),
            ("Heath", 0.04),
            ("Pollard", 0.03),
            ("Lowe", 0.07),
            ("O'Sullivan", 0.04),
            ("Buckley", 0.05),
            ("Bond", 0.05),
            ("Dennis", 0.03),
            ("Lewis", 0.25),
            ("Weston", 0.04),
            ("Joyce", 0.03),
            ("Reynolds", 0.09),
            ("Bishop", 0.06),
            ("Norris", 0.04),
            ("Barry", 0.03),
            ("Whittaker", 0.04),
            ("Carey", 0.03),
            ("Hill", 0.22),
            ("Kent", 0.04),
            ("Ashton", 0.04),
            ("Wilkinson", 0.13),
            ("Powell", 0.12),
            ("Henderson", 0.06),
            ("Freeman", 0.06),
            ("Dunn", 0.07),
            ("Kaur", 0.09),
            ("French", 0.04),
            ("Parry", 0.06),
            ("Walton", 0.06),
            ("Fisher", 0.1),
            ("Naylor", 0.03),
            ("Duffy", 0.04),
            ("Humphreys", 0.04),
            ("Randall", 0.03),
            ("Bevan", 0.03),
            ("Doherty", 0.03),
            ("Moore", 0.21),
            ("Armstrong", 0.07),
            ("Sullivan", 0.05),
            ("Swift", 0.03),
            ("Pearce", 0.09),
            ("Tyler", 0.03),
            ("Bradshaw", 0.04),
            ("Allen", 0.19),
            ("Mellor", 0.03),
            ("Whitehead", 0.05),
            ("Jackson", 0.24),
            ("Grant", 0.07),
            ("Fox", 0.09),
            ("Wright", 0.28),
            ("Anderson", 0.13),
            ("Foster", 0.13),
            ("Gibbs", 0.04),
            ("Butler", 0.11),
            ("Jenkins", 0.1),
            ("John", 0.04),
            ("Morrison", 0.04),
            ("Talbot", 0.03),
            ("Blackburn", 0.03),
            ("Osborne", 0.05),
            ("Flynn", 0.04),
            ("Richards", 0.14),
            ("Hurst", 0.03),
            ("Bibi", 0.05),
            ("Houghton", 0.03),
            ("Johnson", 0.34),
            ("Yates", 0.06),
            ("Mistry", 0.03),
            ("Donnelly", 0.03),
            ("Parkinson", 0.04),
            ("Thomson", 0.05),
            ("Woods", 0.07),
            ("Todd", 0.04),
            ("Dawson", 0.08),
            ("Hart", 0.07),
            ("Graham", 0.1),
            ("Berry", 0.07),
            ("Willis", 0.05),
            ("Miah", 0.04),
            ("Brooks", 0.09),
            ("Horton", 0.03),
            ("Riley", 0.07),
            ("Lambert", 0.05),
            ("Waters", 0.04),
            ("Lynch", 0.05),
            ("Moss", 0.06),
            ("Slater", 0.05),
            ("Knowles", 0.04),
            ("Benson", 0.03),
            ("Adams", 0.13),
            ("King", 0.2),
            ("Davies", 0.48),
            ("Richardson", 0.15),
            ("Vincent", 0.03),
            ("Holmes", 0.11),
            ("Conway", 0.03),
            ("Marshall", 0.14),
            ("Faulkner", 0.03),
            ("Garner", 0.03),
            ("Booth", 0.08),
            ("Harrison", 0.2),
            ("Campbell", 0.11),
            ("Cole", 0.08),
            ("Goddard", 0.04),
            ("Walters", 0.05),
            ("Ellis", 0.13),
            ("Edwards", 0.27),
            ("Peters", 0.04),
            ("Atkinson", 0.08),
            ("Wood", 0.24),
            ("Briggs", 0.04),
            ("Elliott", 0.09),
            ("Chandler", 0.03),
            ("Hope", 0.03),
            ("Hunter", 0.07),
            ("Newman", 0.07),
            ("Pratt", 0.03),
            ("Rahman", 0.03),
            ("Hicks", 0.04),
            ("Cox", 0.14),
            ("Reid", 0.07),
            ("Morris", 0.21),
            ("Banks", 0.04),
            ("Myers", 0.03),
            ("Mitchell", 0.16),
            ("Davey", 0.04),
            ("Peacock", 0.03),
            ("Reed", 0.07),
            ("Carter", 0.15),
            ("Miller", 0.14),
            ("Perkins", 0.04),
            ("Read", 0.05),
            ("Hilton", 0.03),
            ("Moran", 0.03),
            ("Welch", 0.03),
            ("Vaughan", 0.04),
            ("Clements", 0.03),
            ("Griffin", 0.05),
            ("Russell", 0.1),
            ("O'Donnell", 0.03),
            ("Hobbs", 0.03),
            ("Marsh", 0.07),
            ("Porter", 0.07),
            ("Gill", 0.08),
            ("Leonard", 0.03),
            ("McKenzie", 0.03),
            ("Thornton", 0.04),
            ("Fitzgerald", 0.03),
            ("Greenwood", 0.05),
            ("Pearson", 0.1),
            ("James", 0.19),
            ("Coles", 0.03),
            ("Roberts", 0.33),
            ("Nelson", 0.05),
            ("Forster", 0.03),
            ("Gough", 0.03),
            ("Mann", 0.05),
            ("Law", 0.03),
            ("Barker", 0.1),
            ("Cartwright", 0.04),
            ("Bradley", 0.08),
            ("Sharp", 0.05),
            ("Warren", 0.06),
            ("Summers", 0.03),
            ("Little", 0.04),
            ("Perry", 0.08),
            ("Fuller", 0.04),
            ("West", 0.09),
            ("Mason", 0.12),
            ("Finch", 0.03),
            ("Norton", 0.03),
            ("Burke", 0.05),
            ("Holden", 0.04),
            ("Lee", 0.2),
            ("Smart", 0.04),
            ("Bull", 0.04),
            ("Bryant", 0.04),
            ("Gray", 0.12),
            ("Watts", 0.08),
            ("Brady", 0.03),
            ("Baker", 0.2),
            ("Barton", 0.05),
            ("Davis", 0.17),
            ("Baxter", 0.05),
            ("Taylor", 0.53),
            ("Carr", 0.07),
            ("Wong", 0.04),
            ("Cameron", 0.03),
            ("Gardiner", 0.03),
            ("Hawkins", 0.07),
            ("Shaw", 0.15),
            ("Wallace", 0.05),
            ("Young", 0.16),
            ("Shah", 0.06),
            ("Gregory", 0.07),
            ("Ball", 0.08),
            ("Norman", 0.04),
            ("Lawrence", 0.09),
            ("Bowen", 0.04),
            ("Wheeler", 0.05),
            ("Bartlett", 0.04),
            ("Sutton", 0.06),
            ("Lyons", 0.03),
            ("Hutchinson", 0.05),
            ("Poole", 0.05),
            ("Cooke", 0.06),
            ("Franklin", 0.03),
            ("Howe", 0.04),
            ("Walker", 0.27),
            ("Johnston", 0.05),
            ("Austin", 0.05),
            ("Chadwick", 0.03),
            ("Bell", 0.15),
            ("Wall", 0.04),
            ("Woodward", 0.05),
            ("Preston", 0.04),
            ("Bennett", 0.16),
            ("Murray", 0.1),
            ("Begum", 0.13),
            ("McDonald", 0.06),
            ("Hudson", 0.07),
            ("Cross", 0.06),
            ("Singh", 0.13),
            ("Howarth", 0.03),
            ("Hewitt", 0.05),
            ("Curtis", 0.06),
            ("Harding", 0.07),
            ("May", 0.05),
            ("Wells", 0.07),
            ("Giles", 0.03),
            ("Watson", 0.17),
            ("Nolan", 0.03),
            ("Andrews", 0.09),
            ("Hayward", 0.04),
            ("Schofield", 0.04),
            ("Hunt", 0.12),
            ("Robson", 0.06),
            ("Arnold", 0.05),
            ("Morgan", 0.19),
            ("Coates", 0.03),
            ("Page", 0.07),
            ("Simpson", 0.13),
            ("Stewart", 0.09),
            ("Robinson", 0.29),
            ("Fleming", 0.03),
            ("Scott", 0.18),
            ("Chambers", 0.06),
            ("Turner", 0.23),
            ("Watkins", 0.06),
        )
    )

    prefixes_female = ("Mrs", "Ms", "Miss", "Dr")
    prefixes_male = ("Mr", "Dr")
