import discord


class Adventure:

    def __init__(self):
        pass

    @staticmethod
    def intro_message():
        return "*Witaj nieznajomy. Nazywam się Meskhent i przed tysiącami lat żyłam wśród piasków pustyni. Do Polski " \
               "przybyłam dopiero pod koniec XVI wieku, wraz z przyrodnikiem o imieniu Wawrzyniec Scholz, " \
               "który uwięził mnie w krypcie pod Mohren-Apotheke. Jeśli chcesz mnie uwolnić, udaj się do tego miejsca " \
               "i napisz mi jak nazywał się rzeźbiarz którego pomnik znajduje się obecnie na fasadzie budynku.* "

    @staticmethod
    def first_quest():
        embed = discord.Embed(
            title="Eugeniusz Get-Stankiewicz",
            description="Eugeniusz Get-Stankiewicz to polski malarz, artysta i rzeźbiarz. " \
                        "Zajmował się rysunkiem, grafiką warsztatową i użytkową, miedziorytnictwem, medalierstwem, " \
                        "malarstwem i plakatem.  Często wykorzystywał w swej twórczości motyw głowy (nazywanej "
                        "„Łbem”), o rysach samego artysty. W przestrzeni miejskiej Wrocławia pozostawił "
                        "charakterystyczne dzieła, m.in. Tablicę ku Czci Działań na Prostych Liczbach.",
            color=discord.Color.blue())

        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Płaskorzeźba_"
                                "-_autoportret_Geta-Stankiewicza_fot_BMaliszewska.jpg/321px-Płaskorzeźba_"
                                "-_autoportret_Geta-Stankiewicza_fot_BMaliszewska.jpg")
        embed.add_field(name="Tablica ku Czci Działań na Prostych Liczbach", value="Odnajdź tablicę i napisz mi gdzie "
                                                                                   "ją znalazłeś.", inline=False)
        embed.set_footer(text="Kto pyta nie błądzi")
        return embed
