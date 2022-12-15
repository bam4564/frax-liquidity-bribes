from box import Box

# addresses of contracts / tokens 
addresses = Box({
    "token": {
        "frax": '0x853d955aCEf822Db058eb8505911ED77F175b99e'.lower(), 
        "fxs": '0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0'.lower(), 
        'crvfrax': '0x3175df0976dfa876431c2e9ee6bc45b65d3473cc'.lower(), 
    }, 
    "contract": {
        "fraxbp": '0xdcef968d416a41cdac0ed8702fac8128a64241a2'.lower(), 
    }
})

# Infura endpoint. TODO: Put this in an env file 
url_infura = 'https://mainnet.infura.io/v3/856c3834f317452a82e25bb06e04de18'

# snapshot graphql api 
url_snapshot = 'https://hub.snapshot.org/graphql'
snapshot_api_max_records_per_request = 1000 
snapshot_api_max_skip = 5000

# url to various subgraphs 
url_subgraphs = Box({
    "votium-bribes": 'https://api.thegraph.com/subgraphs/name/convex-community/votium-bribes', 
    "convex": {
        "curve_pools": 'https://api.thegraph.com/subgraphs/name/convex-community/curve-pools', 
        "curve_vol_mainnet": 'https://api.thegraph.com/subgraphs/name/convex-community/volume-mainnet' 
    }

})

# TODO: Figure out how this frax subgraph is useful
# https://api.thegraph.com/subgraphs/name/frax-finance-data/fraxbp-subgraph/graphql
