grammar PrismTemplate;

// Tokens
A : 'A';
AT : '@';
BOOL : 'bool';
CLOCK : 'clock';
CONST : 'const';
CTMC : 'ctmc';
C : 'C';
DOUBLE : 'double';
DTMC : 'dtmc';
E : 'E';
ENDINIT : 'endinit';
ENDINVARIANT : 'endinvariant';
ENDMODULE : 'endmodule';
ENDREWARDS : 'endrewards';
ENDSYSTEM : 'endsystem';
FALSE : 'false';
FORMULA : 'formula';
FILTER : 'filter';
FUNC : 'func';
F : 'F';
GLOBAL : 'global';
G : 'G';
INIT : 'init';
INVARIANT : 'invariant';
I : 'I';
INT : 'int';
LABEL : 'label';
MAX : 'max';
MDP : 'mdp';
MIN : 'min';
MODULE : 'module';
X : 'X';
NONDETERMINISTIC : 'nondeterministic';
PMAX : 'Pmax';
PMIN : 'Pmin';
P : 'P';
PROBABILISTIC : 'probabilistic';
PROB : 'prob';
PTA : 'pta';
RATE : 'rate';
REWARDS : 'rewards';
RMAX : 'Rmax';
RMIN : 'Rmin';
R : 'R';
S : 'S';
STOCHASTIC : 'stochastic';
SYSTEM : 'system';
TRUE : 'true';
U : 'U';
W : 'W';
NOT : '!';
AND : '&';
OR : '|';
IMPLIES : '=>';
IFF : '<=>';
RARROW : '->';
COLON : ':';
SEMICOLON : ';';
COMMA : ',';
DOTS : '..';
LPARENTH : '(';
RPARENTH : ')';
LBRACKET : '[';
RBRACKET : ']';
DLBRACKET : '[[';
DRBRACKET :	']]';
LBRACE : '{';
RBRACE : '}';
EQ : '=';
NE : '!=';
LT : '<';
GT : '>';
DLT : '<<';
DGT : '>>';
LE : '<=';
GE : '>=';
PLUS : '+';
MINUS : '-';
TIMES : '*';
DIVIDE : '/';
PRIME : '\'';
RENAME : '<-';
QMARK : '?';
DQUOTE : '"';
REG_INT : ([1-9]([0-9])*)|('0');
REG_DOUBLE : ([0-9])*('.')?([0-9])+([e,E]([-,+])?([0-9])+)?;
REG_IDENTPRIME : [_a-zA-Z]([_a-zA-Z0-9])*'\'';
REG_IDENT : [_a-zA-Z]([_a-zA-Z0-9])*;
PREPROC :			'#'(~[#])*'#';

WS : [ \n\r\t\u000B\u000C\u0000]+				-> channel(HIDDEN) ;
Block_comment : '/*' (Block_comment|.)*? '*/'	-> channel(HIDDEN) ;
Line_comment : '//' .*? ('\n'|EOF)				-> channel(HIDDEN) ;

expression :
LPARENTH expression RPARENTH
| expression IMPLIES expression
| expression IFF expression
| expression OR expression
| expression AND expression
| NOT expression
| expression EQ expression
| expression NE expression
| expression LT expression
| expression LE expression
| expression GT expression
| expression GE expression
| expression PLUS expression
| expression MINUS expression
| expression TIMES expression
| expression DIVIDE expression
| MINUS expression
| REG_IDENT
| REG_INT
| REG_DOUBLE
| TRUE
| FALSE;

identifier : REG_IDENT;

identifier_prime : REG_IDENTPRIME;

native_type : INT | DOUBLE | BOOL;

program : statements? EOF;

statements : model_type? common_declarations? module_declarations init_declaration?;

model_type : DTMC | CTMC | MDP | PTA;

common_declarations : common_declaration common_declarations?;

common_declaration : global_declaration | constant_declaration | formula_declaration;

constant_declaration : CONST native_type identifier EQ expr_or_replacement SEMICOLON;

formula_declaration : FORMULA identifier EQ expr_or_replacement SEMICOLON;

expr_or_replacement : expression | replacement;

global_declaration : GLOBAL var_declaration;

init_declaration : INIT expression ENDINIT;

module_declarations : module_declaration module_declarations?;

module_declaration : MODULE module_content ENDMODULE;

module_content : identifier module_desc | module_rename;

module_rename : id_assign id_assign_block?;

id_assign : identifier EQ identifier;

id_assign_block : LBRACKET id_assign (COMMA id_assign)* RBRACKET;

module_desc : var_declarations? guard_declarations?;

var_declarations : var_declaration var_declarations?;

var_declaration : identifier COLON (native_type | range_declaration) SEMICOLON;

range_declaration : LBRACKET expression DOTS expression RBRACKET;

guard_declarations: (guard_declaration | replacement) guard_declarations?;

guard_declaration : LBRACKET identifier? RBRACKET expression RARROW (state_updates | guard_updates | no_change) SEMICOLON;

guard_updates : guard_update (PLUS guard_updates)?;

guard_update : expression COLON state_updates;

state_updates : state_update (AND state_updates)?;

state_update : LPARENTH identifier_prime EQ expression RPARENTH;

no_change : TRUE;

replacement : AT(identifier)AT;