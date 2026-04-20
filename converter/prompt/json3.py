json3="""
{
  "definitions": {
    "RT_M_0COSTELEMENT_ATTR": {
      "kind": "entity",
      "elements": {
        "KOKRS": {
          "@EndUserText.label": "Controlling Area",
          "type": "cds.String",
          "length": 4,
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
          "notNull": true
        },
        "KSTAR": {
          "@EndUserText.label": "Cost Element",
          "type": "cds.String",
          "length": 10,
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
          "notNull": true
        },
        "DATETO": {
          "@EndUserText.label": "Valid To Date",
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
          ],
          "key": true,
          "notNull": true
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
        "KATYP": {
          "@EndUserText.label": "Cost element category",
          "type": "cds.String",
          "length": 2,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false
        },
        "EIGEN": {
          "@EndUserText.label": "Cost element attributes",
          "type": "cds.String",
          "length": 8,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false
        },
        "MSEHI": {
          "@EndUserText.label": "Unit of Measurement",
          "type": "cds.String",
          "length": 3,
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
      "@EndUserText.label": "Cost Element Attribute",
      "@ObjectModel.modelingPattern": {
        "#": "DATA_STRUCTURE"
      },
      "@DataWarehouse.remote.connection": "EC3",
      "@DataWarehouse.remote.entity": "SAPI.0COSTELMNT_ATTR",
      "_meta": {
        "dependencies": {
          "folderAssignment": "Folder_BYHLVUXL"
        }
      }
    },
    "LT_M_0COSTELEMENT_ATTR": {
      "kind": "entity",
      "elements": {
        "KOKRS": {
          "@EndUserText.label": "Controlling Area",
          "type": "cds.String",
          "length": 4,
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
          "@Analytics.dimension": true
        },
        "KSTAR": {
          "@EndUserText.label": "Cost Element",
          "type": "cds.String",
          "length": 10,
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
          "@Analytics.dimension": true
        },
        "DATETO": {
          "@EndUserText.label": "Valid To Date",
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
          "notNull": true,
          "@Analytics.dimension": true
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
          ],
          "@Analytics.dimension": true
        },
        "KATYP": {
          "@EndUserText.label": "Cost element category",
          "type": "cds.String",
          "length": 2,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false,
          "@Analytics.dimension": true
        },
        "EIGEN": {
          "@EndUserText.label": "Cost element attributes",
          "type": "cds.String",
          "length": 8,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false,
          "@Analytics.dimension": true
        },
        "MSEHI": {
          "@EndUserText.label": "Unit of Measurement",
          "type": "cds.String",
          "length": 3,
          "@DataWarehouse.native.dataType": "NVARCHAR",
          "@DataWarehouse.capabilities.filter.enabled": false,
          "@Analytics.dimension": true
        }
      },
      "@ObjectModel.supportedCapabilities": [
        {
          "#": "SQL_DATA_SOURCE"
        },
        {
          "#": "ANALYTICAL_DIMENSION"
        }
      ],
      "@EndUserText.label": "Cost Element Attribute",
      "@ObjectModel.modelingPattern": {
        "#": "ANALYTICAL_DIMENSION"
      },
      "_meta": {
        "dependencies": {
          "folderAssignment": "Folder_JPJGTDPT"
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
    "DF_M_0COSTELEMENT_ATTR": {
      "kind": "sap.dis.dataflow",
      "@EndUserText.label": "Cost Element Attribute Data Flow",
      "contents": {
        "description": "DF_M_0COSTELEMENT_ATTR",
        "processes": {
          "source1": {
            "component": "com.sap.database.table.consumer",
            "metadata": {
              "label": "RT_M_0COSTELEMENT_ATTR",
              "x": 123,
              "y": 159,
              "height": 60,
              "width": 120,
              "config": {
                "service": "HANA",
                "hanaConnection": {
                  "configurationType": "Configuration Manager",
                  "connectionID": "$DWC"
                },
                "qualifiedName": "RT_M_0COSTELEMENT_ATTR",
                "dwcEntity": "RT_M_0COSTELEMENT_ATTR",
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
          "projection1": {
            "component": "com.sap.dataflow.projection",
            "metadata": {
              "label": "Projection 1",
              "x": 282,
              "y": 159,
              "height": 60,
              "width": 120,
              "config": {
                "attributeMappings": [
                  {
                    "target": "KOKRS",
                    "expression": "\"KOKRS\""
                  },
                  {
                    "target": "KSTAR",
                    "expression": "\"KSTAR\""
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
                    "target": "KATYP",
                    "expression": "\"KATYP\""
                  },
                  {
                    "target": "EIGEN",
                    "expression": "\"EIGEN\""
                  },
                  {
                    "target": "MSEHI",
                    "expression": "\"MSEHI\""
                  },
                  {
                    "target": "CC_DATEFROM",
                    "expression": "TO_DATE(\"DATEFROM\")"
                  },
                  {
                    "target": "CC_DATETO",
                    "expression": "TO_DATE(\"DATETO\")"
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
          },
          "target1": {
            "component": "com.sap.database.table.producer",
            "metadata": {
              "label": "LT_M_0COSTELEMENT_ATTR",
              "x": 443,
              "y": 159,
              "height": 60,
              "width": 120,
              "config": {
                "service": "HANA",
                "hanaConnection": {
                  "configurationType": "Configuration Manager",
                  "connectionID": "$DWC"
                },
                "qualifiedName": "LT_M_0COSTELEMENT_ATTR",
                "dwcEntity": "LT_M_0COSTELEMENT_ATTR",
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
                    "expression": "\"KOKRS\"",
                    "target": "KOKRS"
                  },
                  {
                    "expression": "\"KSTAR\"",
                    "target": "KSTAR"
                  },
                  {
                    "expression": "\"KATYP\"",
                    "target": "KATYP"
                  },
                  {
                    "expression": "\"EIGEN\"",
                    "target": "EIGEN"
                  },
                  {
                    "expression": "\"MSEHI\"",
                    "target": "MSEHI"
                  },
                  {
                    "expression": "\"CC_DATEFROM\"",
                    "target": "DATEFROM"
                  },
                  {
                    "expression": "\"CC_DATETO\"",
                    "target": "DATETO"
                  }
                ],
                "hanaAdaptedDataset": {
                  "schema": {
                    "genericType": "TABLE",
                    "tableBasedRepresentation": {
                      "attributes": [
                        {
                          "name": "KOKRS",
                          "templateType": "string",
                          "length": 4
                        },
                        {
                          "name": "KSTAR",
                          "templateType": "string",
                          "length": 10
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
                          "name": "KATYP",
                          "templateType": "string",
                          "length": 2
                        },
                        {
                          "name": "EIGEN",
                          "templateType": "string",
                          "length": 8
                        },
                        {
                          "name": "MSEHI",
                          "templateType": "string",
                          "length": 3
                        }
                      ],
                      "uniqueKeys": [
                        {
                          "attributeReferences": [
                            "KOKRS",
                            "KSTAR",
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
          }
        },
        "groups": [],
        "connections": [
          {
            "metadata": {
              "points": "243,189 278.5,189"
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
              "points": "407,189 438,189"
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
        "properties": {},
        "vTypes": {
          "scalar": {
            "string_4": {
              "name": "string_4",
              "description": "String(4)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 4
            },
            "string_10": {
              "name": "string_10",
              "description": "String(10)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 10
            },
            "string_8": {
              "name": "string_8",
              "description": "String(8)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 8
            },
            "string_2": {
              "name": "string_2",
              "description": "String(2)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 2
            },
            "string_3": {
              "name": "string_3",
              "description": "String(3)",
              "vflow.type": "scalar",
              "template": "string",
              "value.length": 3
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
                    "KOKRS": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_4"
                    }
                  },
                  {
                    "KSTAR": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_10"
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
                    "KATYP": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_2"
                    }
                  },
                  {
                    "EIGEN": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_8"
                    }
                  },
                  {
                    "MSEHI": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_3"
                    }
                  }
                ]
              },
              "keys": [
                "KOKRS",
                "KSTAR",
                "DATETO"
              ]
            },
            "projection1_outTable": {
              "name": "projection1_outTable",
              "vflow.type": "table",
              "rows": {
                "components": [
                  {
                    "KOKRS": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_4"
                    }
                  },
                  {
                    "KSTAR": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_10"
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
                    "KATYP": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_2"
                    }
                  },
                  {
                    "EIGEN": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_8"
                    }
                  },
                  {
                    "MSEHI": {
                      "vflow.type": "scalar",
                      "vtype-ID": "$INLINE.string_3"
                    }
                  },
                  {
                    "CC_DATEFROM": {
                      "vflow.type": "scalar",
                      "vtype-ID": "com.sap.core.date"
                    }
                  },
                  {
                    "CC_DATETO": {
                      "vflow.type": "scalar",
                      "vtype-ID": "com.sap.core.date"
                    }
                  }
                ]
              },
              "keys": [
                "KOKRS",
                "KSTAR",
                "DATETO"
              ]
            }
          }
        },
        "metadata": {
          "dwc-isPrimaryKeysProcessed": true,
          "dwc-restartOnFail": false
        },
        "parameters": {},
        "parameterMapping": {}
      },
      "sources": {
        "RT_M_0COSTELEMENT_ATTR": {
          "elements": {
            "KOKRS": {},
            "KSTAR": {},
            "DATETO": {},
            "DATEFROM": {},
            "KATYP": {},
            "EIGEN": {},
            "MSEHI": {}
          }
        }
      },
      "targets": {
        "LT_M_0COSTELEMENT_ATTR": {
          "elements": {
            "KOKRS": {},
            "KSTAR": {},
            "KATYP": {},
            "EIGEN": {},
            "MSEHI": {},
            "DATEFROM": {},
            "DATETO": {}
          }
        }
      },
      "connections": {}
    }
  },
  "$version": "1.0"
}
"""