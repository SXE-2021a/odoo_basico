import os, platform


def cadeaTextoSegunPlataforma(cadeaTextoWindows,cadeaTextoGNULinux):
    if platform.system().lower() == 'windows':
        cadeaTexto = cadeaTextoWindows
    else:
        cadeaTexto = cadeaTextoGNULinux
    return cadeaTexto

def rexistra_log(diaHora,ruta,arquivo,contido):
    if os.path.exists(ruta):
        # a Ruta ten que existir e previamente terlle concedidos permisos a odoo para poder facer modificacións
        with open(os.path.join(ruta, arquivo), 'a') as ficheiro:
             ficheiro.write(diaHora + " " + contido + cadeaTextoSegunPlataforma('\r\n','\n'))

def determinaUsuarioSegunContexto(selfie,contexto):
    if "uid" in contexto:
        usuario = selfie.env['res.users'].search([('id', '=', str(contexto["uid"]))])[0].partner_id.display_name
    else:
        usuario = "Templates"
    return usuario

def convirte_data_hora_de_utc_a_timezone_do_usuario(data_hora_utc_object, tzParaConvertir ):
    import pytz
    # recibe a data hora en formato object
    return pytz.UTC.localize(data_hora_utc_object).astimezone(pytz.timezone(tzParaConvertir))  # hora co horario do usuario en formato object