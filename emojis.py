# Maps Wise Old Man skill/boss keys -> Discord custom emoji tags.
# Format is <:name:id> - the "name" part can be anything readable,
# Discord renders based on the numeric id.

SKILL_EMOJIS = {
    "overall":       "<:overall:720446212356177951>",
    "sailing":       "<:sailing:1437131470698446990>",
    "magic":         "<:magic:706462611243532330>",
    "ranged":        "<:ranged:706462611222429796>",
    "hitpoints":     "<:hitpoints:706462611050332258>",
    "slayer":        "<:slayer:706462611222298654>",
    "agility":       "<:agility:706462611121897483>",
    "construction":  "<:construction:706462610853330986>",
    "defence":       "<:defence:706462611000000589>",
    "farming":       "<:farming:706462611364904980>",
    "strength":      "<:strength:706462610916114483>",
    "woodcutting":   "<:woodcutting:706462611205783562>",
    "fishing":       "<:fishing:706462611415236618>",
    "attack":        "<:attack:706462610840879146>",
    "hunter":        "<:hunter:706462611218366534>",
    "thieving":      "<:thieving:706462611214172240>",
    "mining":        "<:mining:706462611134349413>",
    "prayer":        "<:prayer:706462610949931049>",
    "crafting":      "<:crafting:706462610920308761>",
    "firemaking":    "<:firemaking:706462611209977907>",
    "fletching":     "<:fletching:706462611075629138>",
    "smithing":      "<:smithing:706462610945736706>",
    "cooking":       "<:cooking:706462611075629128>",
    "runecrafting":  "<:runecrafting:706462611327287347>",
    "herblore":      "<:herblore:706462611012583456>",
}

BOSS_EMOJIS = {
    "abyssal_sire":              "<:abyssal_sire:729839920969023519>",
    "alchemical_hydra":          "<:alchemical_hydra:729839921207967765>",
    "amoxliatl":                 "<:amoxliatl:1288593574400622644>",
    "araxxor":                   "<:araxxor:1278337345069781082>",
    "bryophyta":                 "<:bryophyta:1283096848017391646>",
    "cerberus":                  "<:cerberus:729839921401167954>",
    "chaos_elemental":           "<:chaos_elemental:729839921401167916>",
    "chambers_of_xeric":         "<:chambers_of_xeric:729839921640112177>",
    "commander_zilyana":         "<:commander_zilyana:729839921430396970>",
    "corporeal_beast":           "<:corporeal_beast:729839921585717310>",
    "crazy_archaeologist":       "<:crazy_archaeologist:729839922021662822>",
    "deranged_archaeologist":    "<:deranged_archaeologist:729839922139234374>",
    "duke_sucellus":             "<:duke_sucellus:1133832623458881586>",
    "general_graardor":          "<:general_graardor:729839922298618026>",
    "giant_mole":                "<:giant_mole:729839922076319875>",
    "grotesque_guardians":       "<:grotesque_guardians:729839922286166086>",
    "hespori":                   "<:hespori:730169239339794624>",
    "hueycoatl":                 "<:hueycoatl:1288593575969292423>",
    "kalphite_queen":            "<:kalphite_queen:729840084609663027>",
    "kraken":                    "<:kraken:729840084798406767>",
    "kreearra":                  "<:kreearra:729840085033287680>",
    "kril_tsutsaroth":           "<:kril_tsutsaroth:729840084781760574>",
    "lunar_chest":               "<:lunar_chest:1220023608383115275>",
    "mimic":                     "<:mimic:730169728357761145>",
    "obor":                      "<:obor:729840084907589674>",
    "phantom_muspah":            "<:phantom_muspah:1097840588000337973>",
    "royal_titans":              "<:royal_titans:1337779462259085332>",
    "sarachnis":                 "<:sarachnis:729840085377220628>",
    "scorpia":                   "<:scorpia:729840084962115666>",
    "skotizo":                   "<:skotizo:729840085398454273>",
    "spindel":                   "<:venenatis:729840086795157595>",
    "the_gauntlet":              "<:the_gauntlet:729840085473820805>",
    "the_hueycoatl":             "<:the_hueycoatl:1288593575969292423>",
    "the_royal_titans":          "<:the_royal_titans:1337779462259085332>",
    "thermonuclear_smoke_devil": "<:thermonuclear_smoke_devil:729840085729673326>",
    "tztok_jad":                 "<:tztok_jad:729840085805170698>",
    "vardorvis":                 "<:vardorvis:1133832631419670700>",
    "venenatis":                 "<:venenatis:729840086795157595>",
    "wintertodt":                "<:wintertodt:730170636189696071>",
    "zalcano":                   "<:zalcano:729840085587066882>",
    "zulrah":                    "<:zulrah:729840085721284629>",
}

MISC_EMOJIS = {
    "clue_scroll":        "<:clue_scroll:729844134004785204>",
    "collection_log":     "<:collection_log:1334481313801179236>",
}


def skill_emoji(name):
    """Returns the emoji tag for a skill, or empty string if we don't have one."""
    return SKILL_EMOJIS.get(name, "")


def boss_emoji(name):
    """Returns the emoji tag for a boss, or empty string if we don't have one."""
    return BOSS_EMOJIS.get(name, "")


def misc_emoji(name):
    """Returns the emoji tag for a misc item (clue scroll, collection log), or empty string."""
    return MISC_EMOJIS.get(name, "")
