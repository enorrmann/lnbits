from flask import g, render_template

from lnbits.decorators import check_user_exists, validate_uuids
from lnbits.extensions.zap import zap_ext


@zap_ext.route("/")
@validate_uuids(["usr"], required=True)
@check_user_exists()
def index():
    # read certificate and add to view
    with open('tls.cert', 'r') as f:
        file_contents = (f.read())
        print("encoded.decode()")
        lines = file_contents.split("\n")
        num_lines = len(lines)
        cert = ""

        for i, item in enumerate(lines):
            if (i>0 and i<(num_lines-2)):
                print(i)
                print(lines[i])
                cert = cert+lines[i]

        #tr -d '=' | tr '/+' '_-'
        cert = cert.replace("=", "")
        cert = cert.replace("/", "_")
        cert = cert.replace("+", "-")
        print(cert)

    return render_template("zap/index.html", user=g.user,cert=cert)
