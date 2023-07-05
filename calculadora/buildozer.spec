[app]

# (str) Título do seu aplicativo
title = ZeqApp

# (str) Pacote do seu aplicativo (deve ser único em toda a Play Store)
package.name = zeqapp

# (str) Nome de domínio (deve ser único)
package.domain = com.zeqapp

# (list) Lista de arquivos para incluir no pacote
source.include_exts = py

# (str) Versão do seu aplicativo
version = 1.0.0

# (list) Dependências do Python separadas por vírgula
requirements = python==3.11.4,kivy==2.2.1

# (list) Pergunte ao usuário qual versão do Python usar
osx.python_version = 3.11.4

# (list) Dependências externas do sistema separadas por vírgula
android.permissions = INTERNET

# (str) Ícone do aplicativo (caminho relativo ao diretório do projeto)
# icon.filename = path/to/icon.png

# (str) Nome do arquivo de ícone (no diretório do projeto)
# icon.filename = icon.png

# (str) Permissões adicionais do Android
android.permissions = INTERNET

# (list) Bibliotecas adicionais para incluir no pacote
# p4a.source_dir = ../../../kivy

# (list) Diretórios para incluir no pacote
# p4a.local_recipes = ./p4a-recipes/

# (list) Opções adicionais de configuração para a criação do pacote
# p4a.private_build_dir = /tmp/myapp/Build

# (str) Versão do SDK do Android a ser usada
# android.sdk = 19

# (str) Caminho para o NDK do Android
# android.ndk_path = /opt/android-ndk-r19c

# (str) Caminho para o SDK do Java
# jdk.path = /usr/lib/jvm/java-8-oracle

# (list) Bibliotecas compartilhadas do Android para incluir no pacote
# android.add_libs_armeabi_v7a = libs/android.so
# android.add_libs_x86 = libs/android.so
