
define(['text'], function(text){

    var buildMap = {},
        templateExtension = ".hbs",
        tplParse = function(tpl){

            return tpl.replace(
                /(?:__\(['"])(.+?)(?:['"]([ ]*,(.+?))?\))/gi,
                '<span data-i18n="$1" data-vars="$2" />'
            );
//            tpl = tpl.replace(/#%21/g, '#!'); // fix bug firefox
        };

    //API
    return {

        load : function(name, req, onLoad, config) {
            if ( config.isBuild ) {
                onLoad(null);
            } else {
                var path = name.substring(name.lastIndexOf(".")) == templateExtension ? name : name + templateExtension;
                text.get(req.toUrl(path), function(data){
                    if (config.isBuild) {
                        buildMap[name] = data;
                        onLoad(data);
                    } else {
                        onLoad(tplParse(data));
                    }
                });
            }
        },

        //write method based on RequireJS official text plugin by James Burke
        //https://github.com/jrburke/requirejs/blob/master/text.js
        write : function(pluginName, moduleName, write){
            if(moduleName in buildMap){
                var content = buildMap[moduleName];
                write('define("'+ pluginName +'!'+ moduleName +'", function(){ return '+ content +';});\n');
            }
        }

    };
});