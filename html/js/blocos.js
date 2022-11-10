Blockly.Blocks['mover'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("MOVER");
        this.appendDummyInput()
            .appendField("Direcao")
            .appendField(new Blockly.FieldDropdown([["Norte", "N"], ["Sul", "S"], ["Leste", "L"], ["Oeste", "O"]]), "direcao");
        this.appendDummyInput()
            .appendField("Quantidade")
            .appendField(new Blockly.FieldNumber(1, 1, 15), "quantidade");
        this.setInputsInline(false);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['for_repetir'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("repetir")
            .appendField(new Blockly.FieldNumber(2, 1), "i")
            .appendField("vezes");
        this.appendStatementInput("NAME")
            .setCheck(null);
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(270);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['while_enquanto'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("enquanto");
        this.appendValueInput("a")
            .setCheck(null);
        this.appendDummyInput()
            .appendField(new Blockly.FieldDropdown([["=", "="], ["!=", "!="], ["<", "<"], ["<=", "<="], [">", ">"], [">=", ">="]]), "tipo");
        this.appendValueInput("b")
            .setCheck(null);
        this.appendStatementInput("NAME")
            .setCheck(null)
            .appendField("faca");
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(330);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['ler_distancia'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("ler distancia");
        this.setOutput(true, "Number");
        this.setColour(60);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['ler_cor'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("ler cor");
        this.setOutput(true, null);
        this.setColour(330);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['acender_led'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("acender led")
            .appendField(new Blockly.FieldColour("#ffff33"), "cor");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(345);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['virar'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("virar")
            .appendField(new Blockly.FieldAngle(90), "angulo");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(105);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['se_senao'] = {
    init: function () {
        this.appendValueInput("se")
            .setCheck("Boolean")
            .appendField("se");
        this.appendStatementInput("faca")
            .setCheck(null)
            .appendField("faca");
        this.appendDummyInput()
            .appendField("se nao");
        this.appendStatementInput("faca_senao")
            .setCheck(null)
            .appendField("faca");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(195);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['camera_cor'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("cor da camera");
        this.setOutput(true, null);
        this.setColour(230);
        this.setTooltip("Retorna a cor lida pela câmera");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['abrir_garra'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("abrir garra");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(0);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['fechar_garra'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("fechar garra");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(0);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['atribuicao_variavel'] = {
    init: function () {
        this.appendDummyInput()
            .appendField(new Blockly.FieldVariable("var"), "var")
            .appendField("=");
        this.appendValueInput("valor")
            .setCheck(null);
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['variavel'] = {
    init: function () {
        this.appendDummyInput()
            .appendField(new Blockly.FieldVariable("var"), "var");
        this.setOutput(true, null);
        this.setColour(180);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['cor'] = {
    init: function () {
        this.appendDummyInput()
            .appendField(new Blockly.FieldColour("#ffff33"), "NAME");
        this.setOutput(true, null);
        this.setColour(315);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

var toolbox = {
    "kind": "categoryToolbox",
    "contents": [
        {
            "kind": "category",
            "name": "Logica",
            "colour": "0",
            "contents": [
                {
                    "kind": "block",
                    "type": "se_senao"
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
            ]
        },
        {
            "kind": "category",
            "name": "Loop",
            "colour": "45",
            "contents": [
                {
                    "kind": "block",
                    "type": "for_repetir"
                },
                {
                    "kind": "block",
                    "type": "while_enquanto"
                },
            ]
        },
        {
            "kind": "category",
            "name": "Matematica",
            "colour": "90",
            "contents": [
                {
                    "kind": "block",
                    "type": "math_arithmetic"
                },
            ]
        },
        {
            "kind": "category",
            "name": "Valores",
            "colour": "135",
            "contents": [
                {
                    "kind": "block",
                    "type": "math_number",
                    "fields": {
                        "NUM": 123
                    }
                },
                {
                    "kind": "block",
                    "type": "text"
                },
                {
                    "kind": "block",
                    "type": "cor"
                },
            ]
        },
        {
            "kind": "category",
            "name": "Funcoes",
            "colour": "180",
            "contents": [
                {
                    "kind": "block",
                    "type": "mover"
                },
                {
                    "kind": "block",
                    "type": "virar"
                },
                {
                    "kind": "block",
                    "type": "ler_distancia"
                },
                {
                    "kind": "block",
                    "type": "ler_cor"
                },
                {
                    "kind": "block",
                    "type": "acender_led"
                },
                {
                    "kind": "block",
                    "type": "camera_cor"
                },
                {
                    "kind": "block",
                    "type": "abrir_garra"
                },
                {
                    "kind": "block",
                    "type": "fechar_garra"
                },
            ]
        },
        {
            "kind": "category",
            "name": "Variaveis",
            "colour": "225",
            "contents": [
                {
                    "kind": "block",
                    "type": "atribuicao_variavel"
                },
                {
                    "kind": "block",
                    "type": "variavel"
                },
            ]
        },
    ]
};

var demoWorkspace = Blockly.inject('blocklyDiv',
    {
        media: 'https://unpkg.com/blockly/media/',
        toolbox: toolbox
    });

demoWorkspace.addChangeListener(showCode);

Blockly.Python['mover'] = function (block) {
    var dropdown_direcao = block.getFieldValue('direcao');
    var number_quantidade = block.getFieldValue('quantidade');
    
    var code = 'mover(\'' + dropdown_direcao + '\', ' + number_quantidade +')\n';
    return code;
};

Blockly.Python['for_repetir'] = function (block) {
    var number_i = block.getFieldValue('i');
    var statements_name = Blockly.Python.statementToCode(block, 'NAME');
    
    var code = 'for i in range(' + number_i + '):\n' +
               statements_name + '\n';
    return code;
};

Blockly.Python['while_enquanto'] = function (block) {
    var value_a = Blockly.Python.valueToCode(block, 'a', Blockly.Python.ORDER_ATOMIC);
    var dropdown_tipo = block.getFieldValue('tipo');
    if (dropdown_tipo == '=')
        dropdown_tipo = '==';
    var value_b = Blockly.Python.valueToCode(block, 'b', Blockly.Python.ORDER_ATOMIC);
    var statements_name = Blockly.Python.statementToCode(block, 'NAME');
    
    var code = 'while ' + value_a + ' ' + dropdown_tipo + ' ' + value_b + ':\n' +
               statements_name + '\n';
    return code;
};

Blockly.Python['ler_distancia'] = function (block) {
    var code = 'ler_distancia()'
    
    return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['ler_cor'] = function (block) {
    var code = 'ler_cor()';
    
    return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['acender_led'] = function (block) {
    var colour_cor = block.getFieldValue('cor');
    
    var code = 'acender_led(\'' + colour_cor + '\')\n';
    return code;
};

Blockly.Python['virar'] = function (block) {
    var angle_angulo = block.getFieldValue('angulo');
    
    var code = 'virar(' + angle_angulo + ')\n';
    return code;
};

Blockly.Python['se_senao'] = function (block) {
    var value_se = Blockly.Python.valueToCode(block, 'se', Blockly.Python.ORDER_ATOMIC);
    var statements_faca = Blockly.Python.statementToCode(block, 'faca');
    var statements_faca_senao = Blockly.Python.statementToCode(block, 'faca_senao');
    
    var code = 'if ' + value_se + ':\n' +
        statements_faca +
        'else:\n' +
        statements_faca_senao + '\n';
    return code;
};

Blockly.Python['camera_cor'] = function (block) {
    var code = 'ler_cor_camera()';
    return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['abrir_garra'] = function (block) {
    var code = 'abrir_garra()\n';
    return code;
};

Blockly.Python['fechar_garra'] = function (block) {
    var code = 'fechar_garra()\n';
    return code;
};

Blockly.Python['atribuicao_variavel'] = function (block) {
    var variable_var = Blockly.Python.nameDB_.getName(block.getFieldValue('var'), Blockly.Variables.NAME_TYPE);
    var value_valor = Blockly.Python.valueToCode(block, 'valor', Blockly.Python.ORDER_ATOMIC);
    
    var code = variable_var + ' = ' + value_valor + '\n';
    return code;
};

Blockly.Python['variavel'] = function (block) {
    var variable_var = Blockly.Python.nameDB_.getName(block.getFieldValue('var'), Blockly.Variables.NAME_TYPE);

    var code = variable_var;
    return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['cor'] = function (block) {
    var colour_name = block.getFieldValue('NAME');

    var code = '\'' + colour_name + '\'';
    return [code, Blockly.Python.ORDER_ATOMIC];
};


//Aumentar tamanho do workspace
var onresize = function (e) {
    var blocklyArea = document.getElementById('blocklyArea');
    var blocklyDiv = document.getElementById('blocklyDiv');
    var element = blocklyArea;
    // Position blocklyDiv over blocklyArea.
    blocklyDiv.style.width = blocklyArea.offsetWidth + 'px';
    blocklyDiv.style.height = blocklyArea.offsetHeight + 'px';
    Blockly.svgResize(demoWorkspace);
};
window.addEventListener('resize', onresize, false);
onresize();
Blockly.svgResize(demoWorkspace);

function showCode() {
    Blockly.Python.INFINITE_LOOP_TRAP = null;
    var code = Blockly.Python.workspaceToCode(demoWorkspace);
    $('#blocklyCode')[0].innerHTML = code;
}