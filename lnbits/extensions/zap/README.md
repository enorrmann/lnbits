<h1>Zap connect extension!</h1>
<h2>*actually grpc server/rest bridge*</h2>
This is an example extension to help you organise and build you own.

Choices : 
    pip install cryptography ? or require key and cert to the user ?
    require lnd-grpc or avoid lnd-grpc ?


https://github.com/LN-Zap/lndconnect/blob/master/lnd_connect_uri.md

echo 'lndconnect://192.168.0.15:10009?cert='"`grep -v 'CERTIFICATE' tls.cert | tr -d '=' | tr '/+' '_-'`"'&macaroon='"`base64 admin.macaroon | tr -d '=' | tr '/+' '_-'`" | tr -d '\n' | qrencode -o out.png

generado con xxd -plain admin.macaroon  > hex.maca

LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUNTakNDQWZDZ0F3SUJBZ0lRUERvOXlEK25EV2FLc25RQTRQdmJaakFLQmdncWhrak9QUVFEQWpCSk1SOHcKSFFZRFZRUUtFeFpzYm1RZ1lYVjBiMmRsYm1WeVlYUmxaQ0JqWlhKME1TWXdKQVlEVlFRREV4MWxiV2xzYVc4dApTRkF0VUhKdlFtOXZheTE0TXpZd0xUUTBNQzFITVRBZUZ3MHlNREE1TVRneE1EVTFNVFphRncweU1URXhNVE14Ck1EVTFNVFphTUVreEh6QWRCZ05WQkFvVEZteHVaQ0JoZFhSdloyVnVaWEpoZEdWa0lHTmxjblF4SmpBa0JnTlYKQkFNVEhXVnRhV3hwYnkxSVVDMVFjbTlDYjI5ckxYZ3pOakF0TkRRd0xVY3hNRmt3RXdZSEtvWkl6ajBDQVFZSQpLb1pJemowREFRY0RRZ0FFdHhhTmtSZkRVcjlwc3pkcnh6ZVRNT2pJUXo2T3lkRUIxbFozRThmVnJ3TXRFdTI1CkhydDlpb09QSTIzSWpFSE9haml1T2xvTXRLTGo5WHBvcVcrZDJhT0J1VENCdGpBT0JnTlZIUThCQWY4RUJBTUMKQXFRd0V3WURWUjBsQkF3d0NnWUlLd1lCQlFVSEF3RXdEd1lEVlIwVEFRSC9CQVV3QXdFQi96QitCZ05WSFJFRQpkekIxZ2gxbGJXbHNhVzh0U0ZBdFVISnZRbTl2YXkxNE16WXdMVFEwTUMxSE1ZSUpiRzlqWVd4b2IzTjBnZ1IxCmJtbDRnZ3AxYm1sNGNHRmphMlYwZ2dkaWRXWmpiMjV1aHdSL0FBQUJoeEFBQUFBQUFBQUFBQUFBQUFBQUFBQUIKaHdUQXFBQVBoeEQrZ0FBQUFBQUFBTlYxZnhmNzFCM3RNQW9HQ0NxR1NNNDlCQU1DQTBnQU1FVUNJUURkaHFtTwpLRWFsWVArTU5wZFJXY3dZT2JTbnNWZ2lGL29WbWlPeVc3VGxPd0lnVTF1Tks1OUtpUWJjUEtuVTV2ZlMzRWtYClArcFFhSXlZV0g1c3FPTzlvQnc9Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K