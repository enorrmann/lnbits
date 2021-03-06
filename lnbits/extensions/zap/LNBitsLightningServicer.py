from lnbits import bolt11
import time
import codecs
import grpc
import json

from .rpc import rpc_pb2 as ln
from .rpc import rpc_pb2_grpc as lnrpc
import requests

class LNBitsLightningServicer(lnrpc.LightningServicer):
    base_url = 'http://localhost:5000/zap/api/v1/'
    add_invoice_url = 'http://localhost:5000/api/v1/payments'

    
    def DebugContext(self,request,context):
        print("REQUEST")
        print(request)
        print("CONTEXT")
        for key, value in context.invocation_metadata():
            print('Received initial metadata: key=%s value=%s' % (key, value))



    def DoPostWithApiKey(self,url,data,context):
        api_key = self.GetApiKeyId(context)
        print("apiki "+api_key) 
        headers = {
            'X-Api-Key': api_key,
            'Content-Type': 'application/json'
        }
        json_response = requests.post(url, json=data, headers=headers)
        resp = json.loads(json_response.text)
        return resp

    def DoGetWithApiKey(self,url,context):
        api_key = self.GetApiKeyId(context)
        print("apiki "+api_key) 
        headers = {
            'X-Api-Key': api_key,
            'Content-Type': 'application/json'
        }
        json_response = requests.get(url, headers=headers)
        resp = json.loads(json_response.text)
        return resp


    def GetApiKeyId(self,context):
        meta = dict(context.invocation_metadata())
        maca = meta["macaroon"]
        macaded = codecs.decode(maca, "hex").decode('utf-8')
        print (macaded)
        return macaded

    def WalletBalance(self, request, context):

        # json_response = requests.post(self.base_url+'walletbalance')
        # resp = json.loads(json_response.text)
        return ln.WalletBalanceResponse(total_balance=0, confirmed_balance=0, unconfirmed_balance=0)

        """
        return ln.WalletBalanceResponse(
            total_balance=resp["total_balance"],
            confirmed_balance=resp["confirmed_balance"],
            unconfirmed_balance=resp["unconfirmed_balance"])
        """

    def ChannelBalance(self, request, context):
        """lncli: `channelbalance`
        ChannelBalance returns the total funds available across all open channels
        in satoshis.
        """
        print("ChannelBalance 11")
        resp = self.DoPostWithApiKey(self.base_url+'channelbalance',{},context)
        print("ChannelBalance 22")
        print(resp)

        return ln.ChannelBalanceResponse(
            balance=resp["balance"],
            pending_open_balance=0
        )

    def GetTransactions(self, request, context):
        print("XXXX GetTransactions")
        return ln.TransactionDetails(transactions=[])

    def EstimateFee(self, request, context):
        """lncli: `estimatefee`
        EstimateFee asks the chain backend to estimate the fee rate and total fees
        for a transaction that pays to multiple specified outputs.

        When using REST, the `AddrToAmount` map type can be set by appending
        `&AddrToAmount[<address>]=<amount_to_send>` to the URL. Unfortunately this
        map type doesn't appear in the REST API documentation because of a bug in
        the grpc-gateway library.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 4")
        context.set_details('Method not 7!')
        raise NotImplementedError('Method not 8!')

    def SendCoins(self, request, context):
        """lncli: `sendcoins`
        SendCoins executes a request to send coins to a particular address. Unlike
        SendMany, this RPC call only allows creating a single output at a time. If
        neither target_conf, or sat_per_byte are set, then the internal wallet will
        consult its fee model to determine a fee for the default confirmation
        target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 5")
        context.set_details('Method not 9!')
        raise NotImplementedError('Method not 10!')

    def ListUnspent(self, request, context):
        """lncli: `listunspent`
        Deprecated, use walletrpc.ListUnspent instead.

        ListUnspent returns a list of all utxos spendable by the wallet with a
        number of confirmations between the specified minimum and maximum.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 6")
        context.set_details('Method not 11!')
        raise NotImplementedError('Method not 12!')

    def SubscribeTransactions(self, request, context):
        """
        SubscribeTransactions creates a uni-directional stream from the server to
        the client in which any newly discovered transactions relevant to the
        wallet are sent over.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("SubscribeTransactions 7")
        context.set_details('Method not 13!')
        raise NotImplementedError('Method not 14!')

    def SendMany(self, request, context):
        """lncli: `sendmany`
        SendMany handles a request for a transaction that creates multiple specified
        outputs in parallel. If neither target_conf, or sat_per_byte are set, then
        the internal wallet will consult its fee model to determine a fee for the
        default confirmation target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 8")
        context.set_details('Method not 15!')
        raise NotImplementedError('Method not 16!')

    def NewAddress(self, request, context):
        """lncli: `newaddress`
        NewAddress creates a new address under control of the local wallet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("NewAddress 9")
        # context.set_details('Method not 17!') zap call 2
        #return ln.NewAddressResponse(address="dummy")
        raise NotImplementedError('Method not implemented!')

    def SignMessage(self, request, context):
        """lncli: `signmessage`
        SignMessage signs a message with this node's private key. The returned
        signature string is `zbase32` encoded and pubkey recoverable, meaning that
        only the message digest and signature are needed for verification.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 10")
        context.set_details('Method not 19!')
        raise NotImplementedError('Method not 20!')

    def VerifyMessage(self, request, context):
        """lncli: `verifymessage`
        VerifyMessage verifies a signature over a msg. The signature must be
        zbase32 encoded and signed by an active node in the resident node's
        channel database. In addition to returning the validity of the signature,
        VerifyMessage also returns the recovered pubkey from the signature.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 11")
        context.set_details('Method not 21!')
        raise NotImplementedError('Method not 22!')

    def ConnectPeer(self, request, context):
        """lncli: `connect`
        ConnectPeer attempts to establish a connection to a remote peer. This is at
        the networking level, and is used for communication between nodes. This is
        distinct from establishing a channel with a peer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 12")
        context.set_details('Method not 23!')
        raise NotImplementedError('Method not 24!')

    def DisconnectPeer(self, request, context):
        """lncli: `disconnect`
        DisconnectPeer attempts to disconnect one peer from another identified by a
        given pubKey. In the case that we currently have a pending or active channel
        with the target peer, then this action will be not be allowed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 13")
        context.set_details('Method not 25!')
        raise NotImplementedError('Method not 26!')

    def ListPeers(self, request, context):
        print("XXXX ListPeers")
        return ln.ListPeersResponse(peers=[])

    def SubscribePeerEvents(self, request, context):
        """
        SubscribePeerEvents creates a uni-directional stream from the server to
        the client in which any events relevant to the state of peers are sent
        over. Events include peers going online and offline.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 15")
        context.set_details('Method not 29!')
        raise NotImplementedError('Method not 30!')

    def GetInfo(self, request, context):
        chain = ln.Chain(chain="bitcoin", network="mainnet")

        return ln.GetInfoResponse(
            version="0.9",
            commit_hash="assd8sa768d67",
            identity_pubkey="12987612931k2j3bk12",
            alias="sd78sd67f87ds",
            num_pending_channels=0,
            num_active_channels=1,
            num_inactive_channels=0,
            num_peers=0,
            block_height=6,
            block_hash="8a8s7sa87687",
            best_header_timestamp=13,
            synced_to_chain=1,
            synced_to_graph=0,
            chains=[chain]
        )

    def GetRecoveryInfo(self, request, context):
        """* lncli: `getrecoveryinfo`
        GetRecoveryInfo returns information concerning the recovery mode including
        whether it's in a recovery mode, whether the recovery is finished, and the
        progress made so far.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 17")
        context.set_details('Method not 33!')
        raise NotImplementedError('Method not 34!')

    def PendingChannels(self, request, context):
        print("XXXX PendingChannels")
        return ln.ListChannelsResponse(channels=[])

    def ListChannels(self, request, context):
        print("XXXX ListChannels")
        fakeChan = ln.Channel(
            active=True,
            remote_pubkey='lnbits',
            capacity=10000,
            local_balance=5000,
            remote_balance=5000,
        )
        return ln.ListChannelsResponse(channels=[fakeChan])

    def SubscribeChannelEvents(self, request, context):
        print("XXXX SubscribeChannelEvents")
        raise NotImplementedError('Method not 40!')

    def ClosedChannels(self, request, context):
        print("XXXX ClosedChannels")
        return ln.ListChannelsResponse(channels=[])

    def FundingStateStep(self, request, context):
        """
        FundingStateStep is an advanced funding related call that allows the caller
        to either execute some preparatory steps for a funding workflow, or
        manually progress a funding workflow. The primary way a funding flow is
        identified is via its pending channel ID. As an example, this method can be
        used to specify that we're expecting a funding flow for a particular
        pending channel ID, for which we need to use specific parameters.
        Alternatively, this can be used to interactively drive PSBT signing for
        funding for partially complete funding transactions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 24")
        context.set_details('Method not 47!')
        raise NotImplementedError('Method not 48!')

    def ChannelAcceptor(self, request_iterator, context):
        """
        ChannelAcceptor dispatches a bi-directional streaming RPC in which
        OpenChannel requests are sent to the client and the client responds with
        a boolean that tells LND whether or not to accept the channel. This allows
        node operators to specify their own criteria for accepting inbound channels
        through a single persistent connection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 25")
        context.set_details('Method not 49!')
        raise NotImplementedError('Method not 50!')

    def CloseChannel(self, request, context):
        """lncli: `closechannel`
        CloseChannel attempts to close an active channel identified by its channel
        outpoint (ChannelPoint). The actions of this method can additionally be
        augmented to attempt a force close after a timeout period in the case of an
        inactive peer. If a non-force close (cooperative closure) is requested,
        then the user can specify either a target number of blocks until the
        closure transaction is confirmed, or a manual fee rate. If neither are
        specified, then a default lax, block confirmation target is used.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 26")
        context.set_details('Method not 51!')
        raise NotImplementedError('Method not 52!')

    def AbandonChannel(self, request, context):
        """lncli: `abandonchannel`
        AbandonChannel removes all channel state from the database except for a
        close summary. This method can be used to get rid of permanently unusable
        channels due to bugs fixed in newer versions of lnd. This method can also be
        used to remove externally funded channels where the funding transaction was
        never broadcast. Only available for non-externally funded channels in dev
        build.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 27")
        context.set_details('Method not 53!')
        raise NotImplementedError('Method not 54!')

    def SendPayment(self, request_iterator, context):
        """lncli: `sendpayment`
        Deprecated, use routerrpc.SendPaymentV2. SendPayment dispatches a
        bi-directional streaming RPC for sending payments through the Lightning
        Network. A single RPC invocation creates a persistent bi-directional
        stream allowing clients to rapidly send payments through the Lightning
        Network with a single persistent connection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 28")
        context.set_details('Method not 55!')
        raise NotImplementedError('Method not 56!')

    def SendPaymentSync(self, request, context):
        print("XXXX SendPaymentSync")
        self.DebugContext(request,context)
        payment_request = request.payment_request
        params = {
            'out': True,
            'bolt11': payment_request
        }
        resp = self.DoPostWithApiKey(self.add_invoice_url, params, context)
        payment_hash = resp["payment_hash"]
        return ln.SendResponse(payment_hash=bytes.fromhex(payment_hash))

    def SendToRoute(self, request_iterator, context):
        """lncli: `sendtoroute`
        Deprecated, use routerrpc.SendToRouteV2. SendToRoute is a bi-directional
        streaming RPC for sending payment through the Lightning Network. This
        method differs from SendPayment in that it allows users to specify a full
        route manually. This can be used for things like rebalancing, and atomic
        swaps.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 30")
        context.set_details('Method not 59!')
        raise NotImplementedError('Method not 60!')

    def SendToRouteSync(self, request, context):
        """
        SendToRouteSync is a synchronous version of SendToRoute. It Will block
        until the payment either fails or succeeds.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 31")
        context.set_details('Method not 61!')
        raise NotImplementedError('Method not 62!')

    def AddInvoice(self, request, context):
        print("s"+request.memo+"s")
        memo = request.memo
        if not memo:
            memo = "new request"
        params = {
            'out': False,
            'amount': request.value,
            'memo': memo
        }
        invoices = self.GetInvoices(context)
        add_index = len(invoices)+1
        print("AddInvoice")
        test_url = "https://ptsv2.com/t/qu294-1600515698/post"
        resp = self.DoPostWithApiKey(self.add_invoice_url, params, context)
        #resp = self.DoPostWithApiKey(test_url, params, context)
        payment_request = resp["payment_request"]
        decoded = bolt11.decode(payment_request)
        payment_hash = decoded.payment_hash
        rhash = bytes.fromhex(payment_hash)

        return ln.AddInvoiceResponse(
            # add_index=resp["checking_id"], no tengo index en la response de lnbits
            # add_index=int(time.time()),
            add_index=add_index,
            r_hash=rhash,
            payment_request=payment_request
        )

    def GetPaymentFromDbRecord(self, invoice, index):
        try:
            payment = ln.Payment(
                value_sat=int(invoice[2]/1000),
                value=int(invoice[2]/1000),
                creation_date=invoice[5],
                payment_hash=invoice[6],
                payment_request=invoice[7],
                payment_index = index+50
            )
            print ("payment")
            print (payment)
            return payment
        except Exception as inst:
            print ("error ***********")
            print(inst)

    def GetInvoiceFromDbRecord(self, invoice, index):
        payment_request = invoice[6]
        pending = invoice[1]

        # IF IT IS PAID (NOT PENDING)
        if (pending == 0):
            settled = True
            state = ln.Invoice.InvoiceState.SETTLED
            amt_paid_sat = int(invoice[2]/1000)
            settle_date = invoice[5]
        else:
            settled = False
            state = ln.Invoice.InvoiceState.OPEN
            amt_paid_sat = 0
            settle_date = None

        decoded = bolt11.decode(payment_request)
        payment_hash = decoded.payment_hash
        rhash = bytes.fromhex(payment_hash)

        return ln.Invoice(
            value=int(invoice[2]/1000),
            memo=invoice[4],
            creation_date=invoice[5],
            payment_request=invoice[6],
            r_hash=rhash,
            add_index=index,
            expiry=decoded.expiry,
            state=state,
            settled=settled,
            amt_paid_sat=amt_paid_sat,
            settle_date=settle_date
        )

    def GetInvoices(self,context):
        #invoices_response = self.DoPostWithApiKey(self.base_url+'invoices',{},context)
        payments_response = self.DoGetWithApiKey(self.add_invoice_url,context)
        invoices = []
        idx = 0
        for db_invoice in payments_response:
            idx = idx + 1
            invoice = self.GetInvoiceFromDbRecord(db_invoice, idx)
            # list includes payments and invoices (in and out)
            if (invoice.value > 0 ):
                invoices.append(invoice)
            
        return invoices

    def GetPayments(self,context):
        #invoices_response = self.DoPostWithApiKey(self.base_url+'invoices',{},context)
        payments_response = self.DoGetWithApiKey(self.add_invoice_url,context)
        payments = []
        idx = 0
        for db_invoice in payments_response:
            idx = idx + 1
            invoice = self.GetPaymentFromDbRecord(db_invoice, idx)
            # list includes payments and invoices (in and out)
            if (invoice.value_sat < 0):
                invoice.value_sat *= -1   #invert value
                invoice.value *= -1
                payments.append(invoice)
            
        return payments

    def ListInvoices(self, request, context):
        print("XXXX ListInvoices")
        invoices = self.GetInvoices(context)
        return ln.ListInvoiceResponse(invoices=invoices)

    def LookupInvoice(self, request, context):
        """lncli: `lookupinvoice`
        LookupInvoice attempts to look up an invoice according to its payment hash.
        The passed payment hash *must* be exactly 32 bytes, if not, an error is
        returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 34")
        context.set_details('Method not 67!')
        raise NotImplementedError('Method not 68!')

    def SubscribeInvoices(self, request, context):
        while 1:
            time.sleep(5)
            invoices = self.GetInvoices
            for invoice in invoices:
                yield invoice

        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("SubscribeInvoices 35")
        context.set_details('Method not 69!')
        raise NotImplementedError('Method not 70!')

    def DecodePayReq(self, request, context):
        decoded = bolt11.decode(request.pay_req)
        try:
            pr =  ln.PayReq(
                timestamp = int(time.time()),
                destination = decoded.payee,
                payment_hash= decoded.payment_hash,
                num_satoshis = int(decoded.amount_msat/1000),
                expiry = decoded.expiry,
                description = decoded.description,
                description_hash = decoded.description_hash,
                payment_addr = bytes.fromhex(decoded.payee),
                features = {}
            )
        except Exception as inst:
            print ("error")
            print(inst)

        return pr

    def ListPayments(self, request, context):
        """lncli: `listpayments`
        ListPayments returns a list of all outgoing payments.
        """
        print("XXXX ListPayments")

        payments = self.GetPayments(context)
        print (payments)

        return ln.ListPaymentsResponse(payments=payments)

    def DeleteAllPayments(self, request, context):
        """
        DeleteAllPayments deletes all outgoing payments from DB.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 38")
        context.set_details('Method not 75!')
        raise NotImplementedError('Method not 76!')

    def DescribeGraph(self, request, context):
        print("XXXX DescribeGraph")
        return ln.ChannelGraph(nodes=[], edges=[])

    def GetNodeMetrics(self, request, context):
        """lncli: `getnodemetrics`
        GetNodeMetrics returns node metrics calculated from the graph. Currently
        the only supported metric is betweenness centrality of individual nodes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 40")
        context.set_details('Method not 79!')
        raise NotImplementedError('Method not 80!')

    def GetChanInfo(self, request, context):
        """lncli: `getchaninfo`
        GetChanInfo returns the latest authenticated network announcement for the
        given channel identified by its channel ID: an 8-byte integer which
        uniquely identifies the location of transaction's funding output within the
        blockchain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 41")
        context.set_details('Method not 81!')
        raise NotImplementedError('Method not 82!')

    def GetNodeInfo(self, request, context):
        """lncli: `getnodeinfo`
        GetNodeInfo returns the latest advertised, aggregated, and authenticated
        channel information for the specified node identified by its public key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 42")
        context.set_details('Method not 83!')
        raise NotImplementedError('Method not 84!')

    def QueryRoutes(self, request, context):
        """lncli: `queryroutes`
        QueryRoutes attempts to query the daemon's Channel Router for a possible
        route to a target destination capable of carrying a specific amount of
        satoshis. The returned route contains the full details required to craft and
        send an HTLC, also including the necessary information that should be
        present within the Sphinx packet encapsulated within the HTLC.

        When using REST, the `dest_custom_records` map type can be set by appending
        `&dest_custom_records[<record_number>]=<record_data_base64_url_encoded>`
        to the URL. Unfortunately this map type doesn't appear in the REST API
        documentation because of a bug in the grpc-gateway library.
        """

        print("XXXX QueryRoutes")
        route = ln.Route(
            total_fees_msat = 20
        )
        return ln.QueryRoutesResponse(routes=[route])

    def GetNetworkInfo(self, request, context):
        """lncli: `getnetworkinfo`
        GetNetworkInfo returns some basic stats about the known channel graph from
        the point of view of the node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 44")
        context.set_details('Method not 87!')
        raise NotImplementedError('Method not 88!')

    def StopDaemon(self, request, context):
        """lncli: `stop`
        StopDaemon will send a shutdown request to the interrupt handler, triggering
        a graceful shutdown of the daemon.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 45")
        context.set_details('Method not 89!')
        raise NotImplementedError('Method not 90!')

    def SubscribeChannelGraph(self, request, context):
        """
        SubscribeChannelGraph launches a streaming RPC that allows the caller to
        receive notifications upon any changes to the channel graph topology from
        the point of view of the responding node. Events notified include: new
        nodes coming online, nodes updating their authenticated attributes, new
        channels being advertised, updates in the routing policy for a directional
        channel edge, and when channels are closed on-chain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 46")
        context.set_details('Method not 91!')
        raise NotImplementedError('Method not 92!')

    def DebugLevel(self, request, context):
        """lncli: `debuglevel`
        DebugLevel allows a caller to programmatically set the logging verbosity of
        lnd. The logging can be targeted according to a coarse daemon-wide logging
        level, or in a granular fashion to specify the logging for a target
        sub-system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 47")
        context.set_details('Method not 93!')
        raise NotImplementedError('Method not 94!')

    def FeeReport(self, request, context):
        """lncli: `feereport`
        FeeReport allows the caller to obtain a report detailing the current fee
        schedule enforced by the node globally for each channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 48")
        context.set_details('Method not 95!')
        raise NotImplementedError('Method not 96!')

    def UpdateChannelPolicy(self, request, context):
        """lncli: `updatechanpolicy`
        UpdateChannelPolicy allows the caller to update the fee schedule and
        channel policies for all channels globally, or a particular channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 49")
        context.set_details('Method not 97!')
        raise NotImplementedError('Method not 98!')

    def ForwardingHistory(self, request, context):
        """lncli: `fwdinghistory`
        ForwardingHistory allows the caller to query the htlcswitch for a record of
        all HTLCs forwarded within the target time range, and integer offset
        within that time range. If no time-range is specified, then the first chunk
        of the past 24 hrs of forwarding history are returned.

        A list of forwarding events are returned. The size of each forwarding event
        is 40 bytes, and the max message size able to be returned in gRPC is 4 MiB.
        As a result each message can only contain 50k entries. Each response has
        the index offset of the last entry. The index offset can be provided to the
        request to allow the caller to skip a series of records.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 50")
        context.set_details('Method not 99!')
        raise NotImplementedError('Method not 100!')

    def ExportChannelBackup(self, request, context):
        """lncli: `exportchanbackup`
        ExportChannelBackup attempts to return an encrypted static channel backup
        for the target channel identified by it channel point. The backup is
        encrypted with a key generated from the aezeed seed of the user. The
        returned backup can either be restored using the RestoreChannelBackup
        method once lnd is running, or via the InitWallet and UnlockWallet methods
        from the WalletUnlocker service.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 51")
        context.set_details('Method not 101!')
        raise NotImplementedError('Method not 102!')

    def ExportAllChannelBackups(self, request, context):
        """
        ExportAllChannelBackups returns static channel backups for all existing
        channels known to lnd. A set of regular singular static channel backups for
        each channel are returned. Additionally, a multi-channel backup is returned
        as well, which contains a single encrypted blob containing the backups of
        each channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 52")
        context.set_details('Method not 103!')
        raise NotImplementedError('Method not 104!')

    def VerifyChanBackup(self, request, context):
        """
        VerifyChanBackup allows a caller to verify the integrity of a channel backup
        snapshot. This method will accept either a packed Single or a packed Multi.
        Specifying both will result in an error.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 53")
        context.set_details('Method not 105!')
        raise NotImplementedError('Method not 106!')

    def RestoreChannelBackups(self, request, context):
        """lncli: `restorechanbackup`
        RestoreChannelBackups accepts a set of singular channel backups, or a
        single encrypted multi-chan backup and attempts to recover any funds
        remaining within the channel. If we are able to unpack the backup, then the
        new channel will be shown under listchannels, as well as pending channels.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 54")
        context.set_details('Method not 107!')
        raise NotImplementedError('Method not 108!')

    def SubscribeChannelBackups(self, request, context):
        """
        SubscribeChannelBackups allows a client to sub-subscribe to the most up to
        date information concerning the state of all channel backups. Each time a
        new channel is added, we return the new set of channels, along with a
        multi-chan backup containing the backup info for all channels. Each time a
        channel is closed, we send a new update, which contains new new chan back
        ups, but the updated set of encrypted multi-chan backups with the closed
        channel(s) removed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("SubscribeChannelBackups 55")
        context.set_details('Method not 109!')
        raise NotImplementedError('Method not 110!')

    def BakeMacaroon(self, request, context):
        """lncli: `bakemacaroon`
        BakeMacaroon allows the creation of a new macaroon with custom read and
        write permissions. No first-party caveats are added since this can be done
        offline.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 56")
        context.set_details('Method not 111!')
        raise NotImplementedError('Method not 112!')

    def ListMacaroonIDs(self, request, context):
        """lncli: `listmacaroonids`
        ListMacaroonIDs returns all root key IDs that are in use.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 57")
        context.set_details('Method not 113!')
        raise NotImplementedError('Method not 114!')

    def DeleteMacaroonID(self, request, context):
        """lncli: `deletemacaroonid`
        DeleteMacaroonID deletes the specified macaroon ID and invalidates all
        macaroons derived from that ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 58")
        context.set_details('Method not 115!')
        raise NotImplementedError('Method not 116!')

    def ListPermissions(self, request, context):
        """lncli: `listpermissions`
        ListPermissions lists all RPC method URIs and their required macaroon
        permissions to access them.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        print("XXXX 59")
        context.set_details('Method not 117!')
        raise NotImplementedError('Method not 118!')
