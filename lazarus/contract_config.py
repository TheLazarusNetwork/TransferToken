contract_address = "0xe760757f02B81e007f457348b36ACd8E6d1551cd"

contract_abi = [
	{
		"constant": True,
		"inputs": [],
		"name": "defaultOperators",
		"outputs": [
			{
				"name": "",
				"type": "address[]"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "spender",
				"type": "address"
			},
			{
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "operator",
				"type": "address"
			},
			{
				"name": "account",
				"type": "address"
			},
			{
				"name": "amount",
				"type": "uint256"
			},
			{
				"name": "userData",
				"type": "bytes"
			},
			{
				"name": "operatorData",
				"type": "bytes"
			}
		],
		"name": "mintToken",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "ceilingSupply",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "holder",
				"type": "address"
			},
			{
				"name": "recipient",
				"type": "address"
			},
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "granularity",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "_from",
				"type": "address"
			},
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_amount",
				"type": "uint256"
			},
			{
				"name": "_data",
				"type": "bytes"
			},
			{
				"name": "_operatorData",
				"type": "bytes"
			}
		],
		"name": "operatorSend",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "_tokenHolder",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "mSymbol",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "mName",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "_operator",
				"type": "address"
			}
		],
		"name": "authorizeOperator",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "mintableToken",
		"outputs": [
			{
				"name": "remaining",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_amount",
				"type": "uint256"
			},
			{
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "send",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "_ownerAddress",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "recipient",
				"type": "address"
			},
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "_operator",
				"type": "address"
			},
			{
				"name": "_tokenHolder",
				"type": "address"
			}
		],
		"name": "isOperatorFor",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "holder",
				"type": "address"
			},
			{
				"name": "spender",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "_newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "_operator",
				"type": "address"
			}
		],
		"name": "revokeOperator",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "_tokenHolder",
				"type": "address"
			},
			{
				"name": "_amount",
				"type": "uint256"
			},
			{
				"name": "_data",
				"type": "bytes"
			},
			{
				"name": "_operatorData",
				"type": "bytes"
			}
		],
		"name": "operatorBurn",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "_amount",
				"type": "uint256"
			},
			{
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "burn",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "name",
				"type": "string"
			},
			{
				"name": "symbol",
				"type": "string"
			},
			{
				"name": "initialSupply",
				"type": "uint256"
			},
			{
				"name": "upperLimit",
				"type": "uint256"
			},
			{
				"name": "_defaultOperators",
				"type": "address[]"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": False,
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": False,
				"name": "operatorData",
				"type": "bytes"
			}
		],
		"name": "Sent",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": False,
				"name": "operatorData",
				"type": "bytes"
			}
		],
		"name": "Minted",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "from",
				"type": "address"
			},
			{
				"indexed": False,
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": False,
				"name": "operatorData",
				"type": "bytes"
			}
		],
		"name": "Burned",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "tokenHolder",
				"type": "address"
			}
		],
		"name": "AuthorizedOperator",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "tokenHolder",
				"type": "address"
			}
		],
		"name": "RevokedOperator",
		"type": "event"
	}
]
