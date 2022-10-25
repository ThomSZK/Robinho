var toolbox = {
    "kind": "flyoutToolbox",
    "contents": [
        {
            "kind": "block",
            "type": "controls_if"
        },
        {
            "kind": "block",
            "type": "logic_compare"
        },
        {
            "kind": "block",
            "type": "logic_operation"
        },
        {
            "kind": "block",
            "type": "logic_boolean"
        },
        {
            "kind": "block",
            "type": "controls_repeat_ext"
        },
        {
            "kind": "block",
            "type": "math_number",
            "fields": {
                "NUM": 123
            }
        },
        {
            "kind": "block",
            "type": "math_arithmetic"
        },
        {
            "kind": "block",
            "type": "text"
        },
        {
            "kind": "block",
            "type": "text_print"
        }
    ]
};

var demoWorkspace = Blockly.inject('blocklyDiv',
    {
        media: 'https://unpkg.com/blockly/media/',
        toolbox: toolbox
    });