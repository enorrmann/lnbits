<h1>Example Extension</h1>
<h2>*tagline*</h2>
This is an example extension to help you organise and build you own.

Try to include an image
<img src="https://i.imgur.com/9i4xcQB.png">


<h2>If your extension has API endpoints, include useful ones here</h2>

<code>curl -H "Content-type: application/json" -X POST https://YOUR-LNBITS/YOUR-EXTENSION/api/v1/EXAMPLE -d '{"amount":"100","memo":"example"}' -H "X-Api-Key: YOUR_WALLET-ADMIN/INVOICE-KEY"</code>


python3 -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/rpc/*.proto
http://localhost:5000/tpos/api/v1/tposs
/extensionname/urls
https://github.com/LN-Zap/lndconnect/blob/master/lnd_connect_uri.md

echo 'lndconnect://192.168.0.15:10009?cert='"`grep -v 'CERTIFICATE' tls.cert | tr -d '=' | tr '/+' '_-'`"'&macaroon='"`base64 admin.macaroon | tr -d '=' | tr '/+' '_-'`" | tr -d '\n' | qrencode -o out.png

generado con xxd -plain admin.macaroon  > hex.maca

fake macaroon
7e687a3f53084333a1d48bb7a922d45f > base64 : N2U2ODdhM2Y1MzA4NDMzM2ExZDQ4YmI3YTkyMmQ0NWY
N2U2ODdhM2Y1MzA4NDMzM2ExZDQ4YmI3YTkyMmQ0NWY
7e687a3f53084333a1d48bb7a922d45f