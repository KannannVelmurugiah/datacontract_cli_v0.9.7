from datacontract.data_contract import DataContract
from datacontract.lint.resolve import to_yaml


data_contract = DataContract(data_contract_file="./datacontract.yaml")

result = data_contract.import_from_source(format='sql',source='./sample_ddl.sql')
print(result.to_yaml())
