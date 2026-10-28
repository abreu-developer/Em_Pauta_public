'use strict';

// A lista usa paginação renderizada pelo Flask. O backend deve enviar 10 filmes por página.
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.movie-poster, .detail-poster, .gallery-grid img').forEach((image) => {
    image.addEventListener('error', () => {
      image.classList.add('image-unavailable');
      image.alt = 'Imagem indisponível';
      // Evita tentar carregar repetidamente a mesma URL inválida.
      image.removeAttribute('src');
    }, { once: true });
  });

  // WebSocket/Socket.IO: ativado apenas na página de detalhes do filme.
  const detail = document.querySelector('#movie-detail[data-movie-id]');
  if (detail && typeof window.io === 'function') {
    const movieId = detail.dataset.movieId;
    const status = document.querySelector('#socket-status');
    const feed = document.querySelector('#live-feed');
    const socket = window.io({ transports: ['websocket', 'polling'] });

    const setConnectionStatus = (state, label) => {
      if (!status) return;
      status.classList.remove('connected', 'disconnected');
      if (state) status.classList.add(state);
      status.innerHTML = `<i aria-hidden="true"></i> ${label}`;
    };

    socket.on('connect', () => {
      setConnectionStatus('connected', 'WebSocket conectado');
      socket.emit('join_movie', { movie_id: movieId });
    });

    socket.on('disconnect', () => {
      setConnectionStatus('disconnected', 'Conexão interrompida');
    });

    socket.on('connect_error', () => {
      setConnectionStatus('disconnected', 'Não foi possível conectar');
    });

    // Evento esperado do servidor: { movie_id, type, message, timestamp }.
    socket.on('movie_update', (event) => {
      if (!event || String(event.movie_id) !== String(movieId) || !feed) return;
      const empty = feed.querySelector('.feed-empty');
      if (empty) empty.remove();

      const item = document.createElement('li');
      const time = document.createElement('time');
      const now = event.timestamp ? new Date(event.timestamp) : new Date();
      time.textContent = Number.isNaN(now.getTime())
        ? new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })
        : now.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
      const message = document.createElement('span');
      message.textContent = event.message || event.type || 'O filme foi atualizado.';
      item.append(time, message);
      feed.prepend(item);

      // Mantém o feed curto e evita crescimento infinito no navegador.
      while (feed.children.length > 8) feed.lastElementChild.remove();

      // Atualizações opcionais podem modificar dados exibidos, sem inserir HTML remoto.
      if (event.name) {
        const title = document.querySelector('#movie-title');
        if (title) title.textContent = event.name;
        document.title = `${event.name} — CinePauta`;
      }
      if (typeof event.review === 'string') {
        const review = document.querySelector('#movie-review');
        if (review) review.textContent = event.review;
      }
    });

    window.addEventListener('pagehide', () => socket.disconnect(), { once: true });
  }

  const retryButton = document.querySelector('#retry-button');
  if (retryButton) retryButton.addEventListener('click', () => window.location.reload());
});
