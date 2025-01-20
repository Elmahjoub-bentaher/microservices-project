FROM php:8.3.11-fpm

# Mettre à jour la liste des paquets et installer les dépendances
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libpng-dev \
    libjpeg-dev \
    libwebp-dev \
    libxpm-dev \
    libfreetype6-dev \
    libzip-dev \
    zip \
    unzip \
    git \
    bash \
    fcgiwrap \
    libmcrypt-dev \
    libonig-dev \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Installer les extensions PHP
RUN docker-php-ext-configure gd --with-freetype --with-jpeg --with-webp \
    && docker-php-ext-install gd \
    && docker-php-ext-install pdo pdo_mysql mbstring zip exif pcntl bcmath opcache

# Installer Composer
COPY --from=composer/composer:latest-bin /composer /usr/bin/composer

# Créer un dossier pour le cache npm et définir les permissions
RUN mkdir -p /var/www/.npm && chown -R www-data:www-data /var/www/.npm

# Créer un dossier pour VS Code Server et définir les permissions
RUN mkdir -p /var/www/.vscode-server && chown -R www-data:www-data /var/www/.vscode-server

# Copier les fichiers de l'application
COPY --chown=www-data:www-data . /var/www/html/

# Passer à l'utilisateur www-data
USER www-data

# Définir le répertoire de travail
WORKDIR /var/www/html

# Installer les dépendances npm
RUN npm install

# Compiler les assets
RUN npm run build

# Exposer le port 8000
EXPOSE 8000

# Démarrer le serveur Laravel
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]