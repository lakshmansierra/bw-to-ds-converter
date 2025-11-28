json1="""
{
  "definitions": {
    "LT_M_ACCT_TYPE_TEXT": {
      "kind": "entity",
      "elements": {
        "LANGU": {
          "@EndUserText.label": "Language Key",
          "type": "cds.String",
          "length": 1,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.allowedExpressions": [
            {
              "#": "EQUAL"
            },
            {
              "#": "BETWEEN"
            }
          ],
          "key": true,
          "notNull": true,
          "@Semantics.language": true
        },
        "KEY1": {
          "@EndUserText.label": "Key Field for DataSource for Text",
          "type": "cds.String",
          "length": 60,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.allowedExpressions": [
            {
              "#": "EQUAL"
            },
            {
              "#": "BETWEEN"
            }
          ],
          "key": true,
          "notNull": true,
          "@ObjectModel.text.element": [
            {
              "=": "TXTLG"
            }
          ]
        },
        "TXTLG": {
          "@EndUserText.label": "Long description",
          "type": "cds.String",
          "length": 60,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false,
          "@Semantics.text": true
        },
        "CC_TEXT": {
          "@EndUserText.label": "Text Column",
          "type": "cds.String",
          "length": 20
        }
      },
      "@ObjectModel.supportedCapabilities": [
        {
          "#": "SQL_DATA_SOURCE"
        },
        {
          "#": "LANGUAGE_DEPENDENT_TEXT"
        }
      ],
      "@EndUserText.label": "Account Type",
      "@ObjectModel.modelingPattern": {
        "#": "LANGUAGE_DEPENDENT_TEXT"
      },
      "_meta": {
        "dependencies": {
          "folderAssignment": null
        }
      }
    },
    "RT_M_ACCT_TYPE_TEXT": {
      "kind": "entity",
      "@DataWarehouse.remote.connection": "EC3",
      "@DataWarehouse.remote.entity": "SAPI.0ACCT_TYPE_TEXT",
      "elements": {
        "LANGU": {
          "type": "cds.String",
          "length": 1,
          "@DataWarehouse.capabilities.filter.allowedExpressions": [
            {
              "#": "EQUAL"
            },
            {
              "#": "BETWEEN"
            }
          ],
          "@EndUserText.label": "Language Key",
          "@DataWarehouse.native.dataType": "NVARCHAR"
        },
        "KEY1": {
          "type": "cds.String",
          "length": 60,
          "@DataWarehouse.capabilities.filter.allowedExpressions": [
            {
              "#": "EQUAL"
            },
            {
              "#": "BETWEEN"
            }
          ],
          "@EndUserText.label": "Key Field for DataSource for Text",
          "@DataWarehouse.native.dataType": "NVARCHAR"
        },
        "TXTLG": {
          "type": "cds.String",
          "length": 60,
          "@DataWarehouse.capabilities.filter.enabled": false,
          "@EndUserText.label": "Long description",
          "@DataWarehouse.native.dataType": "NVARCHAR"
        }
      },
      "@ObjectModel.modelingPattern": {
        "#": "DATA_STRUCTURE"
      },
      "@ObjectModel.supportedCapabilities": [
        {
          "#": "DATA_STRUCTURE"
        },
        {
          "#": "SQL_DATA_SOURCE"
        }
      ],
      "@EndUserText.label": "Account Type",
      "_meta": {
        "dependencies": {
          "folderAssignment": null
        }
      }
    }
  },
  "version": {
    "csn": "1.0"
  },
  "meta": {
    "creator": "CDS Compiler v1.19.2"
  },
  "dataflows": {
    "DF_M_ACCT_TYPE_TEXT": {
      "kind": "sap.dis.dataflow",
      "@EndUserText.label": "Account type Data Flow",
      "contents": {
        "properties": {},
        "metadata": {
          "dwc-isPrimaryKeysProcessed": true,
          "dwc-restartOnFail": false
        },
        "parameters": {},
        "parameterMapping": {},
        "description": "DF_M_ACCT_TYPE_TEXT",
        "processes": {
          "source1": {
            "component": "com.sap.database.table.consumer",
            "metadata": {
              "label": "RT_M_ACCT_TYPE_TEXT",
              "x": 35,
              "y": 214,
              "height": 60,
              "width": 120,
              "config": {
                "service": "HANA",
                "hanaConnection": {
                  "configurationType": "Configuration Manager",
                  "connectionID": "$DWC"
                },
                "qualifiedName": "RT_M_ACCT_TYPE_TEXT",
                "dwcEntity": "RT_M_ACCT_TYPE_TEXT",
                "remoteObjectType": "TABLE",
                "fetchSize": 1000,
                "forceFetchSize": false,
                "failOnStringTruncation": true
              },
              "outports": [
                {
                  "name": "outTable",
                  "type": "table",
                  "vtype-ID": "$INLINE.source1_outTable"
                }
              ]
            }
          },
          "target1": {
            "component": "com.sap.database.table.producer",
            "metadata": {
              "label": "LT_M_ACCT_TYPE_TEXT",
              "x": 372,
              "y": 215,
              "height": 60,
              "width": 120,
              "config": {
                "service": "HANA",
                "hanaConnection": {
                  "configurationType": "Configuration Manager",
                  "connectionID": "$DWC"
                },
                "qualifiedName": "LT_M_ACCT_TYPE_TEXT",
                "dwcEntity": "LT_M_ACCT_TYPE_TEXT",
                "remoteObjectType": "TABLE",
                "fetchSize": 1000,
                "forceFetchSize": false,
                "failOnStringTruncation": true,
                "mode": "append",
                "upsert": true,
                "batchSize": 1000,
                "forceBatchSize": false,
                "attributeMappings": [
                  {
                    "expression": "\"LANGU\"",
                    "target": "LANGU"
                  },
                  {
                    "expression": "\"KEY1\"",
                    "target": "KEY1"
                  },
                  {
                    "expression": "\"TXTLG\"",
                    "target": "TXTLG"
                  },
                  {
                    "expression": "\"CC_TEXT\"",
                    "target": "CC_TEXT"
                  }
                ],
                "hanaAdaptedDataset": {
                  "schema": {
                    "genericType": "TABLE",
                    "tableBasedRepresentation": {
                      "attributes": [
                        {
                          "name": "LANGU",
                          "templateType": "string",
                          "length": 1
                        },
                        {
                          "name": "KEY1",
                          "templateType": "string",
                          "length": 60
                        },
                        {
                          "name": "TXTLG",
                          "templateType": "string",
                          "length": 60
                        },
                        {
                          "name": "CC_TEXT",
                          "templateType": "string",
                          "length": 20
                        }
                      ],
                      "uniqueKeys": [
                        {
                          "attributeReferences": [
                            "LANGU",
                            "KEY1"
                          ]
                        }
                      ]
                    }
                  }
                }
              },
              "inports": [
                {
                  "name": "inTable",
                  "type": "table",
                  "vtype-ID": "$INLINE.projection1_outTable"
                }
              ]
            }
          },
          "projection1": {
            "component": "com.sap.dataflow.projection",
            "metadata": {
              "label": "Projection 1",
              "x": 197,
              "y": 214,
              "height": 60,
              "width": 120,
              "config": {
                "attributeMappings": [
                  {
                    "target": "LANGU",
                    "expression": "\"LANGU\""
                  },
                  {
                    "target": "KEY1",
                    "expression": "\"KEY1\""
                  },
                  {
                    "target": "TXTLG",
                    "expression": "\"TXTLG\""
                  },
                  {
                    "target": "CC_TEXT",
                    "expression": "'E'"
                  }
                ]
              },
              "inports": [
                {
                  "name": "inTable",
                  "type": "table",
                  "vtype-ID": "$INLINE.source1_outTable"
                }
              ],
              "outports": [
                {
                  "name": "outTable",
                  "type": "table",
                  "vtype-ID": "$INLINE.projection1_outTable"
                }
              ]
            }
          }
        },
        "groups": [],
        "connections": [
          {
            "metadata": {
              "points": "155,244 193.5,244"
            },
            "src": {
              "port": "outTable",
              "process": "source1"
            },
            "tgt": {
              "port": "inTable",
              "process": "projection1"
            }
          },
          {
            "metadata": {
              "points": "322,244 344.5,244 344.5,245 367,245"
            },
            "src": {
              "port": "outTable",
              "process": "projection1"
            },
            "tgt": {
              "port": "inTable",
              "process": "target1"
            }
          }
        ],
        "inports": {},
        "outports": {},
        "vTypes": {
          "scalar": {
            "string_1": {
              "name": "string_1",
              "description": "String(1)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 1
            },
            "string_60": {
              "name": "string_60",
              "description": "String(60)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 60
            },
            "string_2": {
              "name": "string_2",
              "description": "String(2)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 2
            }
          },
          "structure": {},
          "table": {
            "source1_outTable": {
              "name": "source1_outTable",
              "vflow.type": "table",
              "rows": {
                "components": [
                  {
                    "LANGU": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_1"
                    }
                  },
                  {
                    "KEY1": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_60"
                    }
                  },
                  {
                    "TXTLG": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_60"
                    }
                  }
                ]
              }
            },
            "projection1_outTable": {
              "name": "projection1_outTable",
              "vflow.type": "table",
              "rows": {
                "components": [
                  {
                    "LANGU": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_1"
                    }
                  },
                  {
                    "KEY1": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_60"
                    }
                  },
                  {
                    "TXTLG": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_60"
                    }
                  },
                  {
                    "CC_TEXT": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_2"
                    }
                  }
                ]
              }
            }
          }
        }
      },
      "sources": {
        "RT_M_ACCT_TYPE_TEXT": {
          "elements": {
            "LANGU": {},
            "KEY1": {},
            "TXTLG": {}
          }
        }
      },
      "targets": {
        "LT_M_ACCT_TYPE_TEXT": {
          "elements": {
            "LANGU": {},
            "KEY1": {},
            "TXTLG": {},
            "CC_TEXT": {}
          }
        }
      },
      "connections": {}
    }
  },
  "$version": "1.0"
}
"""