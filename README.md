# Valid JSON File Script
> 1. Check the JSON is a valid JSON
> 2. Check the JSON type is correct
> 3. Using configuration to judge JSON property

```yaml
result:
  j_type: "object"
  j_value:
    data:
      j_type: "array"
      required: 1
      j_value:
        - type: "object"
          required: 1
          j_value:
            name:
              j_type: [ "string" ]
              required: 1
            age:
              j_type: [ "string" ]
              required: 1
            score:
              j_type: "integer"
              required: 1
              max: 100
              min: 40
            parent:
              j_type: "object"
              required: 1
              j_value:
                name:
                  required: 1
                  j_type: ["string"]
```

## config.yaml 文件配置

### `number`类型

> 1. `integer `: 整型
> 2. `number`:  浮点、小数类型
> 3. `range`: 表示数值限制[1, 8, 32]
> 4. `min`: 最小值
> 5. `max`: 最大值

### `string`类型

> 1. `range`： 表示支持字符串的类型,
> 2. `min`:  最小字符串长度
> 3. `max`: 最大字符串长度

### `array`类型

### `object`

> 1. 对象类型
> 2. `required`代表是否是必须检查属性