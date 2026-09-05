import cytoscape from 'cytoscape';

for (const root of document.querySelectorAll('[data-qp-graph]')) {
  if (root.dataset.ready) continue;
  const view = root.querySelector('[data-graph-view]');
  const controls = root.querySelector('[data-graph-controls]');
  const status = root.querySelector('[data-graph-status]');
  const select = root.querySelector('select');
  try {
    const model = JSON.parse(root.querySelector('[data-graph-data]').textContent);
    const nodes = model.elements.filter(({ data }) => data.source === undefined);
    const edgeCount = model.elements.length - nodes.length;
    view.hidden = false;
    const cy = cytoscape({
      container: view,
      elements: model.elements,
      minZoom: 0.15,
      maxZoom: 3,
      wheelSensitivity: 0.2,
      layout: { name: 'breadthfirst', directed: model.directed, animate: false, padding: 32 },
      style: [
        { selector: 'node', style: { label: 'data(label)', 'text-wrap': 'wrap', 'text-max-width': 140, 'font-size': 14, color: '#172033', 'background-color': '#90b8e8', width: 36, height: 36 } },
        { selector: 'edge', style: { label: 'data(label)', 'font-size': 11, color: '#24384f', 'text-background-color': '#ffffff', 'text-background-opacity': 1, 'text-background-padding': 2, width: 2, 'line-color': '#657d95', 'target-arrow-color': '#657d95', 'target-arrow-shape': model.directed ? 'triangle' : 'none', 'curve-style': 'bezier' } },
        { selector: ':selected', style: { 'border-width': 4, 'border-color': '#16457a', 'line-color': '#16457a' } },
      ],
    });
    const announce = () => { status.textContent = `${nodes.length} nodes, ${edgeCount} relationships. Full text remains below.`; };
    select.addEventListener('change', () => {
      cy.elements().unselect();
      if (!select.value) { cy.fit(undefined, 32); announce(); return; }
      const selected = cy.getElementById(select.value);
      selected.select();
      cy.center(selected);
      status.textContent = `Selected ${selected.data('label')}.`;
    });
    cy.on('tap', 'node', (event) => {
      select.value = event.target.id();
      select.dispatchEvent(new Event('change'));
    });
    root.querySelector('[data-graph-fit]').addEventListener('click', () => { cy.fit(undefined, 32); announce(); });
    for (const button of root.querySelectorAll('[data-graph-zoom]')) {
      button.addEventListener('click', () => {
        const level = Math.max(cy.minZoom(), Math.min(cy.maxZoom(), cy.zoom() * Number(button.dataset.graphZoom)));
        cy.zoom({ level, renderedPosition: { x: cy.width() / 2, y: cy.height() / 2 } });
        status.textContent = `Zoom ${Math.round(level * 100)}%.`;
      });
    }
    controls.hidden = false;
    root.dataset.ready = 'true';
    announce();
  } catch {
    view.hidden = true;
    controls.hidden = true;
    root.dataset.ready = 'unavailable';
    status.textContent = 'Interactive view unavailable. All supplied nodes, relationships and sources remain below.';
  }
}
