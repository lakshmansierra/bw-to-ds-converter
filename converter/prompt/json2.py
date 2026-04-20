json2="""

{
  "definitions": {
    "LT_M_0JOB_TEXT": {
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
              "=": "TXTMD"
            }
          ]
        },
        "DATETO": {
          "@EndUserText.label": "Valid-to date",
          "type": "cds.Date",
          "@DataWarehouse.native.dataType": "VARCHAR",
          "@DataWarehouse.capabilities.filter.allowedExpressions": [
            {
              "#": "EQUAL"
            },
            {
              "#": "BETWEEN"
            }
          ],
          "key": true,
          "notNull": true
        },
        "DATEFROM": {
          "@EndUserText.label": "Valid-From Date",
          "type": "cds.Date",
          "@DataWarehouse.native.dataType": "VARCHAR",
          "@DataWarehouse.capabilities.filter.allowedExpressions": [
            {
              "#": "EQUAL"
            },
            {
              "#": "BETWEEN"
            }
          ]
        },
        "TXTSH": {
          "@EndUserText.label": "Short description",
          "type": "cds.String",
          "length": 20,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false
        },
        "TXTMD": {
          "@EndUserText.label": "Medium description",
          "type": "cds.String",
          "length": 40,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false,
          "@Semantics.text": true
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
      "@EndUserText.label": "Job Text",
      "@ObjectModel.modelingPattern": {
        "#": "LANGUAGE_DEPENDENT_TEXT"
      },
      "_meta": {
        "dependencies": {
          "folderAssignment": "Folder_JPJGTDPT"
        }
      }
    },
    "RT_M_0JOB_TEXT": {
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
          ]
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
          ]
        },
        "DATETO": {
          "@EndUserText.label": "Valid-to date",
          "type": "cds.String",
          "length": 8,
          "@DataWarehouse.native.dataType": "VARCHAR",
          "@DataWarehouse.capabilities.filter.allowedExpressions": [
            {
              "#": "EQUAL"
            },
            {
              "#": "BETWEEN"
            }
          ]
        },
        "DATEFROM": {
          "@EndUserText.label": "Valid-From Date",
          "type": "cds.String",
          "length": 8,
          "@DataWarehouse.native.dataType": "VARCHAR",
          "@DataWarehouse.capabilities.filter.allowedExpressions": [
            {
              "#": "EQUAL"
            },
            {
              "#": "BETWEEN"
            }
          ]
        },
        "TXTSH": {
          "@EndUserText.label": "Short description",
          "type": "cds.String",
          "length": 20,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false
        },
        "TXTMD": {
          "@EndUserText.label": "Medium description",
          "type": "cds.String",
          "length": 40,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false
        }
      },
      "@ObjectModel.supportedCapabilities": [
        {
          "#": "SQL_DATA_SOURCE"
        },
        {
          "#": "DATA_STRUCTURE"
        }
      ],
      "@EndUserText.label": "Job Text",
      "@ObjectModel.modelingPattern": {
        "#": "DATA_STRUCTURE"
      },
      "@DataWarehouse.remote.connection": "EC3",
      "@DataWarehouse.remote.entity": "SAPI.0JOB_TEXT",
      "_meta": {
        "dependencies": {
          "folderAssignment": "Folder_BYHLVUXL"
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
    "DF_M_0JOB_TEXT": {
      "kind": "sap.dis.dataflow",
      "@EndUserText.label": "Job Text Data Flow",
      "contents": {
        "properties": {},
        "metadata": {
          "dwc-isPrimaryKeysProcessed": true,
          "dwc-restartOnFail": false
        },
        "parameters": {},
        "parameterMapping": {},
        "description": "DF_M_0JOB_TEXT",
        "processes": {
          "source1": {
            "component": "com.sap.database.table.consumer",
            "metadata": {
              "label": "RT_M_0JOB_TEXT",
              "x": 40,
              "y": 144,
              "height": 60,
              "width": 120,
              "config": {
                "service": "HANA",
                "hanaConnection": {
                  "configurationType": "Configuration Manager",
                  "connectionID": "$DWC"
                },
                "qualifiedName": "RT_M_0JOB_TEXT",
                "dwcEntity": "RT_M_0JOB_TEXT",
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
              "label": "LT_M_0JOB_TEXT",
              "x": 364,
              "y": 149,
              "height": 60,
              "width": 120,
              "config": {
                "service": "HANA",
                "hanaConnection": {
                  "configurationType": "Configuration Manager",
                  "connectionID": "$DWC"
                },
                "qualifiedName": "LT_M_0JOB_TEXT",
                "dwcEntity": "LT_M_0JOB_TEXT",
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
                    "expression": "\"TXTSH\"",
                    "target": "TXTSH"
                  },
                  {
                    "expression": "\"TXTMD\"",
                    "target": "TXTMD"
                  },
                  {
                    "expression": "\"CC_DATETO\"",
                    "target": "DATETO"
                  },
                  {
                    "expression": "\"CC_DATEFROM\"",
                    "target": "DATEFROM"
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
                          "name": "DATETO",
                          "templateType": "date"
                        },
                        {
                          "name": "DATEFROM",
                          "templateType": "date"
                        },
                        {
                          "name": "TXTSH",
                          "templateType": "string",
                          "length": 20
                        },
                        {
                          "name": "TXTMD",
                          "templateType": "string",
                          "length": 40
                        }
                      ],
                      "uniqueKeys": [
                        {
                          "attributeReferences": [
                            "LANGU",
                            "KEY1",
                            "DATETO"
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
              "y": 144,
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
                    "target": "DATETO",
                    "expression": "\"DATETO\""
                  },
                  {
                    "target": "DATEFROM",
                    "expression": "\"DATEFROM\""
                  },
                  {
                    "target": "TXTSH",
                    "expression": "\"TXTSH\""
                  },
                  {
                    "target": "TXTMD",
                    "expression": "\"TXTMD\""
                  },
                  {
                    "target": "CC_DATETO",
                    "expression": "TO_DATE(\"DATETO\")"
                  },
                  {
                    "target": "CC_DATEFROM",
                    "expression": "TO_DATE(\"DATEFROM\")"
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
              "points": "160,174 193.5,174"
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
              "points": "317,176.5 360.5,176.5"
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
            "string_8": {
              "name": "string_8",
              "description": "String(8)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 8
            },
            "string_20": {
              "name": "string_20",
              "description": "String(20)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 20
            },
            "string_40": {
              "name": "string_40",
              "description": "String(40)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 40
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
                    "DATETO": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_8"
                    }
                  },
                  {
                    "DATEFROM": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_8"
                    }
                  },
                  {
                    "TXTSH": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_20"
                    }
                  },
                  {
                    "TXTMD": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_40"
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
                    "DATETO": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_8"
                    }
                  },
                  {
                    "DATEFROM": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_8"
                    }
                  },
                  {
                    "TXTSH": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_20"
                    }
                  },
                  {
                    "TXTMD": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_40"
                    }
                  },
                  {
                    "CC_DATETO": {
                      "vflow.type": "scalar",
                      "vtype-ID": "com.sap.core.date"
                    }
                  },
                  {
                    "CC_DATEFROM": {
                      "vflow.type": "scalar",
                      "vtype-ID": "com.sap.core.date"
                    }
                  }
                ]
              }
            }
          }
        }
      },
      "sources": {
        "RT_M_0JOB_TEXT": {
          "elements": {
            "LANGU": {},
            "KEY1": {},
            "DATETO": {},
            "DATEFROM": {},
            "TXTSH": {},
            "TXTMD": {}
          }
        }
      },
      "targets": {
        "LT_M_0JOB_TEXT": {
          "elements": {
            "LANGU": {},
            "KEY1": {},
            "TXTSH": {},
            "TXTMD": {},
            "DATETO": {},
            "DATEFROM": {}
          }
        }
      },
      "connections": {}
    }
  },
  "$version": "1.0"
}
"""