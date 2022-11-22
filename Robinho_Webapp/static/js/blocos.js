Blockly.Blocks['mover'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("MOVER");
        this.appendDummyInput()
            .appendField("Direcao")
            .appendField(new Blockly.FieldDropdown([["Frente", "F"], ["Tras", "T"]]), "direcao");
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
        var field = new Blockly.FieldColour('#ffff00');
        field.setColours(
            ['#00ff00', '#ffff00', '#ff0000', '#ff00ff', '#0000ff', '#00ffff', '#ffffff'],
            ['verde', 'amarelo', 'vermelho', 'rosa', 'azul', 'ciano', 'branco']);
        this.appendDummyInput()
            .appendField("acender led")
            .appendField(field, "cor");
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
            .appendField(new Blockly.FieldDropdown([["direita", "D"], ["esquerda", "E"]]), "direcao");
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
        var field = new Blockly.FieldColour('#ffff00');
        field.setColours(
            ['#00ff00', '#ffff00', '#ff0000', '#ff00ff', '#0000ff', '#00ffff', '#ffffff'],
            ['verde', 'amarelo', 'vermelho', 'rosa', 'azul', 'ciano', 'branco']);
        this.appendDummyInput()
            .appendField(field, "NAME");
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

    var cod_dir = null;
    if (dropdown_direcao == 'F')
        cod_dir = '00';
    else if (dropdown_direcao == 'T')
        cod_dir = '01';

    code = 'for i in range (' + number_quantidade + '):\n' +
        '  robinho_func.arduino_cmd(0b000111' + cod_dir + ', uart)\n';

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

Blockly.Python['ler_cor'] = function (block) {
    var code = 'robinho_func.read_floor_color(uart)';

    return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['acender_led'] = function (block) {
    var colour_cor = block.getFieldValue('cor');

    var r = colour_cor.substring(1, 3);
    var g = colour_cor.substring(3, 5);
    var b = colour_cor.substring(5, 7);

    var digito_r = 0, digito_g = 0, digito_b = 0;

    if (r == 'ff')
        digito_r = 1;
    if (g == 'ff')
        digito_g = 1;
    if (b == 'ff')
        digito_b = 1;

    var code = 'robinho_func.arduino_cmd(0b' + digito_r.toString() + digito_g.toString() + digito_b.toString() + '11000, uart)\n';

    return code;
};

Blockly.Python['virar'] = function (block) {
    var dropdown_direcao = block.getFieldValue('direcao');

    var cod_dir = null;
    if (dropdown_direcao == 'D')
        cod_dir = '10';
    else if (dropdown_direcao == 'E')
        cod_dir = '11';

    var code = 'robinho_func.arduino_cmd(0b000111' + cod_dir + ', uart)\n';

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
    var code = 'robinho_func.read_camera_color(uart);\n';
    return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['abrir_garra'] = function (block) {
    var code = 'robinho_func.arduino_cmd(0b00011010, uart);\n';
    return code;
};

Blockly.Python['fechar_garra'] = function (block) {
    var code = 'robinho_func.arduino_cmd(0b00011011, uart);\n';
    return code;
};

Blockly.Python['atribuicao_variavel'] = function (block) {
    var variable_var = Blockly.Python.nameDB_.getName(block.getFieldValue('var'), Blockly.Names.NameType.VARIABLE);
    var value_valor = Blockly.Python.valueToCode(block, 'valor', Blockly.Python.ORDER_ATOMIC);

    var code = variable_var + ' = ' + value_valor + '\n';
    return code;
};

Blockly.Python['variavel'] = function (block) {
    var variable_var = Blockly.Python.nameDB_.getName(block.getFieldValue('var'), Blockly.Names.NameType.VARIABLE);

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

function gerarArquivo() {
    var codigo = 'import machine\n' +
        'import socket\n' +
        'import time\n' +
        'import camera\n' +
        'import robinho_func\n' +
        'from machine import Pin\n' +
        'from machine import UART\n\n' +
        'flash = Pin(4, Pin.OUT)\n' +
        'uart = machine.UART(1, 9600, rx=12, tx=13)\n' +
        'uart.init(9600, bits=8, parity=None, stop=1)\n' +
        'uart.read()\n\n' +
        'client_socket = socket.socket()\n' +
        'client_socket.connect(("10.0.0.102", 93))\n' +
        'client_socket.settimeout(0.1)\n' +
        'robinho_func.blink(0.2, flash)\n\n' +
        $('#blocklyCode')[0].innerHTML + '\n' +
        'client_socket.close()\n';

    var userInput = codigo;

    var blob = new Blob([userInput], { type: "text/plain" });
    saveAs(blob, "main.py");
}
